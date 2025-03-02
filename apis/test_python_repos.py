import requests
import json

def test_github_api():
    url = "https://api.github.com/search/repositories"
    url += "?q=language:javascript+sort:stars+stars:>10000"

    headers = {"Accept": "application/vnd.github.v3+json"} # V3 api and json format
    r = requests.get(url, headers=headers) # make request and assign response object(mainly status code, headers and content) to variable r
    print(f"Status code: {r.status_code}") # response object attribute called status code

    assert r.status_code == 200

    # Convert the response object to a dictionary and process overall results
    response_dict = r.json()
    print(f"Complete results: {not response_dict['incomplete_results']}")

    # Explore information avout the repositories
    repo_dicts = response_dict['items']
    repo_links, stars, hover_texts = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        stars.append(repo_dict['stargazers_count'])

    assert len(stars) == len(repo_dicts) and len(repo_dicts) == 30
