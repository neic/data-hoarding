#!/usr/bin/python3
import requests
import os

API_KEY = os.getenv("GOOGLE_API_KEY")
CHANNEL_ID = os.getenv("YT_CHANNEL_ID")
CHANNEL_FILE = os.getenv("CHANNEL_FILE")


def get_subscriptions(pageToken=None):

    r = requests.get(
        "https://www.googleapis.com/youtube/v3/subscriptions/",
        params={
            "part": "snippet",
            "maxResults": 50,
            "channelId": CHANNEL_ID,
            "key": API_KEY,
            "pageToken": pageToken,
        },
    )
    r.raise_for_status()
    resp = r.json()

    channels = [s["snippet"]["resourceId"]["channelId"] for s in resp["items"]]

    if "nextPageToken" in resp:
        channels.extend(get_subscriptions(resp["nextPageToken"]))

    return channels


def write_file(channels):
    with open(CHANNEL_FILE, "w") as fp:
        for channel in channels:
            fp.write("https://www.youtube.com/channel/%s\n" % channel)


if __name__ == "__main__":
    print("Updating list of subscriptions for channel %s" % CHANNEL_ID)
    channels = get_subscriptions()
    write_file(channels)
    print("Sucessfully updated %s" % CHANNEL_FILE)
