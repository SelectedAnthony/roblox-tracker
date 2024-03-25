# variables:

webhook = 'https://discord.com/api/webhooks/1221940949291237567/SMbPUs1ASwhljG_0Nsg4_uQ06_pXlZhG-Lt8fCOMbZ4N-q4HZjdZ3IFPqZcL4HLPoe0c' # set your discord webhook here
user_id = 'yarmee0' # set the roblox user's username you wanna track
minutes_per_check = 1 # minutes per check

# code below !!!

import requests, time

track = requests.get(f'https://api.roblox.com/users/{user_id}/onlinestatus').json()
info = requests.get(f'https://users.roblox.com/v1/users/{user_id}').json()

last_online = track['LastOnline']

while True:
    time.sleep(minutes_per_check*60)
    track = requests.get(f'https://api.roblox.com/users/{user_id}/onlinestatus').json()
    if last_online != track['LastOnline']:
        requests.post(webhook, json={f'content':f'@here {info["name"]} logged in at {info["LastOnline"]}'})
        last_online = track['LastOnline']
    if track["IsOnline"] == True:
        requests.post(webhook, json={ 'content': '@everyone', 'embeds': [ { 'title': 'Roblox Tracker', 'description': f'Account: <https://www.roblox.com/users/{user_id}/profile>\n{info["name"]} is online! Here\'s everything we know:', 'url': 'https://github.com/mov-ebx/roblox-tracker', 'footer': { 'text': 'https://github.com/mov-ebx/roblox-tracker', 'icon_url': 'https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' } } ] })
