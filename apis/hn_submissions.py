from operator import itemgetter
import requests
import json
import plotly.express as px

# Make an API call and check the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

r = requests.get(url) # make request and assign response object(mainly status code, headers and content) to variable r
print(f"Status code: {r.status_code}") # response object attribute called status code

# Convert the response object to a dictionary and process overall results
submission_ids = r.json()
submission_dicts, submission_titles, submission_comments = [], [], []
for submission_id in submission_ids[:30]:
    # Make a new API call for each id
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r=requests.get(url)
    print(f"id: {submission_id}\status: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': response_dict['url'],
            'comments': response_dict['descendants'],
        }
    except KeyError:
        print(f'not all info found for {submission_id}')
        continue
    submission_dicts.append(submission_dict)
    submission_titles.append(submission_dict['title'])
    submission_comments.append(submission_dict['comments'])

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                         reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"hn_link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# Make visualization
title = "Most-Commented Articles on Hacker News Home Page"
labels = {'x': 'Article', 'y': 'Comments'}
fig = px.bar(x=submission_titles, y=submission_comments, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
            yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=.6)
fig.show()






# response_string = json.dumps(response_dict, indent=4)
# print(response_string)


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


