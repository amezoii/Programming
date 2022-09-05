import requests
import json

#below is my PAT for my test ADO. I'm not worried about you having it for testing the current authentication method. However, I think a lot of people are moving to MSAL
pat = ''
url = 'https://dev.azure.com/amezoii/_apis/wit/workitems?ids=242&fields=System.Title,System.State,System.AssignedTo,System.Tags&api-version=7.1-preview.3'

#auth and api call to the URL
response = requests.get(url,
    # headers={'Content-Type': 'json'},
    auth=('', pat))

data = response.json()

x = json.dumps(data, indent=2, sort_keys=True)
print(x)