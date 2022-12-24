import json
from PIL import Image
import requests
from io import BytesIO
import os
import time


def get_image_size(href):
    try:
        response = requests.get(href)
        img = Image.open(BytesIO(response.content))
        return img.width, img.height
    except Exception as e:
        print(e)
        return 0, 0


def ffz_api_global(emotes):
    url = "https://api.frankerfacez.com/v1/set/global"
    response = requests.get(url)
    data = response.json()
    for key in data["sets"]:
        for data_emote in data["sets"][key]["emoticons"]:
            emotes[data_emote['id']] = {}
            for scale in ["1", "2", "4"]:
                href = f"https://cdn.frankerfacez.com/emote/{data_emote['id']}/{scale}"
                w, h = get_image_size(href)
                if w != 0 and h != 0:
                    # print(f"{data_emote['name']} - {scale}x -> {w}x{h}")
                    emotes[data_emote['id']][scale] = {"w": w, "h": h, "href": href}


def ffz_api_channel(emotes, streamid):
    url = "https://api.frankerfacez.com/v1/room/id/" + str(streamid)
    response = requests.get(url)
    data = response.json()
    if "message" in data:
        # print(f"ERR: {data['message']}")
        return
    if "sets" in data:
        for key in data["sets"]:
            for data_emote in data["sets"][key]["emoticons"]:
                emotes[data_emote['id']] = {}
                for scale in ["1", "2", "4"]:
                    href = f"https://cdn.frankerfacez.com/emote/{data_emote['id']}/{scale}"
                    w, h = get_image_size(href)
                    if w != 0 and h != 0:
                        # print(f"{data_emote['name']} - {scale}x -> {w}x{h}")
                        emotes[data_emote['id']][scale] = {"w": w, "h": h, "href": href}


def export_data(data):
    dir = "./data/"
    if not os.path.exists(dir):
        os.makedirs(dir)
    outpath = dir + "ffz_emotes.json"
    with open(outpath, "w") as f:
        json.dump(data, f, indent=2)
        print(f"FFZ: Saving into: {outpath}")


# array of all our emotes we have
emotes = {}
time_start = time.time()

# global api endpoint
ffz_api_global(emotes)
print(f"FFZ: global emotes done ({len(emotes)} so far)")
print(f"======================================================")

# loop through each streamer!
filestreamers = "./data/top_streamers.json"
if os.path.exists(filestreamers):
    data = json.load(open(filestreamers))
    for key in data:
        streamobj = data[key]
        ffz_api_channel(emotes, streamobj['user_id'])
        print(f"FFZ: {streamobj['username']} channel emotes done ({len(emotes)} so far)")
        if int(key) % 10 == 0:
            export_data(emotes)
        print(f"======================================================")

# print how long the script took
export_data(emotes)
print(f"FFZ: Took {round((time.time() - time_start) / 60.0, 2)} minutes to complete...")
