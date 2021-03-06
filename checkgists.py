import json
import requests

# Load old gists in from gists.json if possible
try:
    with open('gists.json') as input_file:
        previous_gists = json.load(input_file)
except Exception as e:
    print "Failed to load previous gists in:", e
    previous_gists = []

# make a list of the previously seen gist IDs
previous_gist_ids = {}
for gist in previous_gists:
    previous_gist_ids[gist['id']] = True

# fetch all gists
url = "https://api.github.com/users/james-portman/gists"
headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
gists = response.json()

# check for new gists we haven't seen
for gist in gists:
    if gist['id'] not in previous_gist_ids:
        print "Found a new gist:"
        print gist['html_url']

# Save all found gists to gists.json
with open('gists.json', 'w') as output_file:
    json.dump(gists, output_file)
