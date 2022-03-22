import requests
import os

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth(os.environ['REDCLIENT_ID'], os.environ['REDSECRET_TOKEN'])
print(auth)
# here we pass our login method (password), username, and password
data = {
    'grant_type': 'password',
    'username': os.environ['REDUSERNAME'],
    'password': os.environ['REDPASSWORD']
}
print(data)
# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'JamesBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth,
                    data=data,
                    headers=headers)
print(res)
print(res.json())
# convert response to JSON and pull access_token value
REDTOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {REDTOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)


async def redShitPost():
    res = requests.get("https://oauth.reddit.com/r/python/hot",
                       headers=headers)

    print(res.json())
