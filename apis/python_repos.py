import requests

# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"} # V3 api and json format
r = requests.get(url, headers=headers) # make request and assign response object(mainly status code, headers and content) to variable r
print(f"Status code: {r.status_code}") # response object attribute called status code

# Convert the response object to a dictionary
response_dict = r.json()

# Process the results
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information avout the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Description: {repo_dict['description']}")
