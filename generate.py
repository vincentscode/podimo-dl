from typing import List

import requests
import re

js_url = "https://podimo.com/_nuxt/ff1590b.js"
js_studio_urls = [
    "https://studio.podimo.com/449.595c8ccdc7c0ebc7631b.js",
    "https://studio.podimo.com/d353d7b3d943b1220974.js"
]

r = requests.get(js_url)
js_txt = str(r.content.decode('utf-8','ignore').encode("utf-8"))


def cleanup(match: str) -> str:
    match = match.replace("\\\\n", "\n")
    match = match.replace("\\\\t", "\t")
    match = match[1:-1]
    
    indent = re.search(r"[^\s]", match).start()-1
    match = '\n'.join([l[indent:] for l in match.split("\n")])
    return match

def find_quote_with_substring(search_string: str, substring: str) -> List[str]:
    return [cleanup(x) for x in re.findall(f'"([^"]*{substring}[^"]*)"', search_string)]


def cleanup_js(match: str) -> str:
    match = match.replace("\\n", "\n")
    match = match.replace("\\t", "\t")
    indent = re.search(r"[^\s]", match).start()-1
    match = '\n'.join([l[indent:] for l in match.split("\n")])
    return match


def find_js_quote_with_substring(search_string: str, substring: str) -> List[str]:
    return [cleanup_js(x) for x in re.findall(f'`([^`]*{substring}[^`]*)`', search_string)]


def get_name(match: str) -> str:
    return re.findall(r"\t?[A-z]* ([A-z_]*)[ \(\{]", match.strip().split("\n")[0])[0]


queries = []
mutations = []

for url in js_studio_urls:
    r = requests.get(url)
    js_studio_txt = str(r.content.decode('utf-8','ignore').encode("utf-8"))
    for q in find_js_quote_with_substring(js_studio_txt, "query "):
        queries.append(q)

    for m in find_js_quote_with_substring(js_studio_txt, "mutation "):
        queries.append(m)

for q in find_quote_with_substring(js_txt, "query "):
    queries.append(q)

for m in find_quote_with_substring(js_txt, "mutation "):
    queries.append(m)


query_template = "\nquery{} = gql('''\n{}''')\n"
f = open("queries.py", "w")
f.write("from gql import gql\n")
for q in queries:
    name = get_name(q)
    f.write(query_template.format(name, q))
f.close()

mutation_template = "\nmutation{} = gql('''\n{}''')\n"
f = open("mutations.py", "w")
f.write("from gql import gql\n")
for m in find_quote_with_substring(js_txt, "mutation "):
    name = get_name(m)
    f.write(mutation_template.format(name, m))
f.close()
