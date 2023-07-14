from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import urllib.request
import argparse
import os
import re
import eyed3
from pathlib import Path
from mutations import *
from queries import *

class PodimoAPI:
    def __init__(self):
        self.transport1 = AIOHTTPTransport(url="https://studio.podimo.com/graphql")
        self.transport2 = AIOHTTPTransport(url="https://podimo.com/graphql")
        self.client1 = Client(transport=self.transport1, fetch_schema_from_transport=False)
        self.client2 = Client(transport=self.transport2, fetch_schema_from_transport=False)

    def login(self, email, password, is_creator):
        if is_creator:
            result = self.client1.execute(queryTokenWithCredentials, variable_values={
                'email': email,
                'password': password,
                'scope': 'CREATOR',
            })
        else:
            result = self.client.execute(queryTokenWithCredentials, variable_values={
                'email': email,
                'password': password,
            })

        token = result["tokenWithCredentials"]["token"]
        self.transport1.headers = self.transport2.headers = {
            'accept': '*/*',
            'user-os': 'android',
            'user-locale': 'en-US',
            'user-agent': 'okhttp/4.9.1',
            'Host': 'graphql.pdm-gateway.com',
            'authorization': token,
        }

    def search_podcast(self, search_query, region="de"):
        result = self.client2.execute(queryUsePodcastsExistQuery, variable_values={
            'search': search_query,
            'region': region
        })
        search_result = [r for r in result["publicSearch"] if search_query in r["title"]]
        if len(search_result) > 0:
            return search_result[0]
        return None

    def get_podcast_episodes(self, podcast_id, limit=1000, offset=0):
        result = self.client.execute(queryPodcastEpisodes, variable_values={
            'podcastId': podcast_id,
            'limit': limit,
            'offset': offset,
        })
        return result["podcastEpisodes"]


    def download_episode(self, podcast_episode, output_folder=None, overwrite=False):
        name = podcast_episode["title"]
        url = podcast_episode["audio"]["url"]

        sane_name = "".join([c for c in name if c.isalpha() or c.isdigit() or c in ' #']).rstrip()
        fn = f'{sane_name}.mp3'
        if output_folder:
            fn = f'{output_folder}/{fn}'

        if not overwrite and os.path.exists(fn):
            print(f"Skipping {name}. File already exists. (Overwrite with --overwrite)")
            return fn

        print(f"Downloading {name} from {url}...")
        mp3file =  urllib.request.urlopen(url)
        with open(fn, 'wb') as output:
            output.write(mp3file.read())
        return fn

def do_it_question(question):
    xy = input(question + " (Y/n) > ")
    return not xy.lower() == "n"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--podcast", )
    parser.add_argument("-c", "--config", action="store_true")
    parser.add_argument("-d", "--download", action="store_true")
    parser.add_argument("--premium-only", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()

    if (args.config and os.path.exists("config.py")) or do_it_question("Use config.py?"):
        from config import email, password, is_creator
    else:
        email = input("Email > ")
        password = input("Password > ")
        is_creator = False

    podimo = PodimoAPI()
    podimo.login(email, password, is_creator)

    if not args.podcast:
        search_string = input("Podcast Name > ")
    else:
        search_string = args.podcast

    podcast = podimo.search_podcast(search_string)
    if not podcast:
        print("Not found!")
        return

    episodes = podimo.get_podcast_episodes(podcast["id"])

    if args.premium_only:
        episodes = [x for x in filter(lambda e: e["accessLevel"] == "PREMIUM", episodes)]

    for e in episodes:
        print(" > ", e["title"])

    if args.download or do_it_question("Download Episodes?"):
        for e in episodes:
            fn = podimo.download_episode(e, args.output, args.overwrite)

            title_with_track_num = re.match(r"^#?([0-9]{1,}) (.+)", e["title"])
            if title_with_track_num:
                track_num, title = title_with_track_num.groups()
            else:
                track_num, title = (0, e["title"])

            audiofile = eyed3.load(fn)
            audiofile.tag.title = title
            audiofile.tag.publisher = "Podimo"
            audiofile.tag.comments.set(e["description"])
            audiofile.tag.original_release_date = audiofile.tag.release_date = e["datetime"].replace(".000Z", "Z").split("T")[0]
            audiofile.tag.track_num = track_num
            audiofile.tag.save(version=eyed3.id3.ID3_V2_4)

if __name__ == '__main__':
    main()
