import requests
import json

base_url = 'https://v2.sherpa.ac.uk/cgi/retrieve_by_id'

journal = 'scientific reports'

issn = '2045-2322'

api_key = 'XXXXXXXXX'

full_url = base_url + '?item-type=publication&api-key=' + api_key + '&format=Json&identifier=' + journal


response = requests.get(full_url)

x = response.json()

print(x)
