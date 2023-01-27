#importing the necessary libraries
import requests
import json
import time
import urllib

#setting the token for the bot
TOKEN = "5961186050:AAFLW57la19tvwiwVfHlLKoVWFk_ng0uNj0"

#defining the url
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

#function to get the latest update
def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    response = requests.get(url)
    return json.loads(response.content)

#function to get the latest update
def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

#function to send a message
def send_message(text, chat_id):
    url = URL + "sendMessage?chat_id={}&text={}".format(chat_id, text)
    requests.get(url)

#function to send an image
def send_image(image_url, chat_id):
    url = URL + "sendPhoto?chat_id={}&photo={}".format(chat_id, image_url)
    requests.get(url)

#function to measure the speed of the server
def measure_server_speed(url, chat_id):
    start = time.time()
    resp = urllib.urlopen(url)
    end = time.time()
    download_speed = resp.info().getheader('Content-Length')
    if download_speed is not None:
        download_speed = float(download_speed) / (end - start) / 1000
    send_message("The server download speed is {} GB/s".format(download_speed), chat_id)
    send_image(url, chat_id)

#main function
def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            chat_id = updates["result"][-1]["message"]["chat"]["id"]
            text = updates["result"][-1]["message"]["text"]
            if "speed" in text:
                measure_server_speed("http://example.com/image.jpg", chat_id)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
