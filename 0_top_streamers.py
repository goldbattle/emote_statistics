import json
import requests
import os



# todo: is this the best url??
url = "https://twitchpayouts.com/api/payouts"
response = requests.get(url)
data = response.json()
print(f"{len(data)} total streamers in top list")

# finally export to file
dir = "./data/"
if not os.path.exists(dir):
    os.makedirs(dir)
with open(dir + "top_streamers.json", "w") as f:
    json.dump(data, f, indent=2)


