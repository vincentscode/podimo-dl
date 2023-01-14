from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import urllib.request
from mutations import *
from queries import *

class PodimoAPI:
    def __init__(self):
        self.transport = AIOHTTPTransport(url="https://graphql.pdm-gateway.com/graphql")
        self.client = Client(transport=self.transport, fetch_schema_from_transport=False)

    def login(self, email, password, is_creator):
        if is_creator:
            result = self.client.execute(queryTokenWithCredentialsScoped, variable_values={
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
        self.transport.headers = {
            'accept': '*/*',
            'user-os': 'android',
            'user-locale': 'en-US',
            'user-agent': 'okhttp/4.9.1',
            'Host': 'graphql.pdm-gateway.com',
            'authorization': token,
        }

    def search_podcast(self, search_query, region="de"):
        result = self.client.execute(queryWebDoSearchPodcast, variable_values={
            'search': search_query,
            'region': region
        })
        search_result = [r for r in result["publicSearch"] if search_query in r["title"]]
        if len(search_result) > 0:
            return search_result[0]
        return None

    def get_podcast_episodes(self, podcast_id, limit=1000, offset=0):
        result = self.client.execute(queryPodcastEpisodesQuery, variable_values={
            'podcastId': podcast_id,
            'limit': limit,
            'offset': offset,
        })
        return result["podcastEpisodes"]


    def download_episode(self, podcast_episode):
        name = podcast_episode["title"]
        url = podcast_episode["audio"]["url"]
        print(f"Downloading {name} from {url}...")

        mp3file =  urllib.request.urlopen(url)

        sane_name = "".join([c for c in name if c.isalpha() or c.isdigit() or c==' ']).rstrip()
        with open(f'{sane_name}.mp3','wb') as output:
            output.write(mp3file.read())

def do_it_question(question):
    xy = input(question + " (Y/n) > ")
    return not xy.lower() == "n"

def main():
    if do_it_question("Use config.py?"):
        from config import email, password, is_creator
    else:
        email = input("Email > ")
        password = input("Password > ")
        is_creator = False

    podimo = PodimoAPI()
    podimo.login(email, password, is_creator)

    search_string = input("Podcast Name > ")
    podcast = podimo.search_podcast(search_string)
    if not podcast:
        print("Not found!")
        return

    episodes = podimo.get_podcast_episodes(podcast["id"])
    for e in episodes:
        print(" > ", e["title"])

    if do_it_question("Download Episodes?"):
        for e in episodes:
            podimo.download_episode(e)

if __name__ == '__main__':
    main()
