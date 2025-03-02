import requests
import json
import plotly.express as px

# Make an API call and check the response
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"

headers = {"Accept": "application/vnd.github.v3+json"} # V3 api and json format
r = requests.get(url, headers=headers) # make request and assign response object(mainly status code, headers and content) to variable r
print(f"Status code: {r.status_code}") # response object attribute called status code

# Convert the response object to a dictionary and process overall results
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)


# print(f"Complete results: {not response_dict['incomplete_results']}")

# # Explore information avout the repositories
# repo_dicts = response_dict['items']
# repo_links, stars, hover_texts = [], [], []
# for repo_dict in repo_dicts:
#     repo_name = repo_dict['name']
#     repo_url = repo_dict['html_url']
#     repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
#     repo_links.append(repo_link)
#     stars.append(repo_dict['stargazers_count'])

#     # Build hover texts.
#     owner = repo_dict['owner']['login']
#     description = repo_dict['description']
#     hover_text = f"{owner}<br />{description}"
#     hover_texts.append(hover_text)

# # Make visualization
# title = "Most-Starred Python Projects on Github"
# labels = {'x': 'Repository', 'y': 'Stars'}
# fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

# fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
#             yaxis_title_font_size=20)

# fig.update_traces(marker_color='SteelBlue', marker_opacity=.6)
# fig.show()
