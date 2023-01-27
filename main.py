import speedtest
import telegram
import time

bot_token = '5961186050:AAFLW57la19tvwiwVfHlLKoVWFk_ng0uNj0'
bot = telegram.Bot(token = bot_token)

def test_speed():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    download_speed = res["download"]
    upload_speed = res["upload"]
    ping_time = res["ping"]
    return (download_speed, upload_speed, ping_time)

def send_speed(download_speed, upload_speed, ping_time):
    message = "Server speed test results: \nDownload speed: {} Mbps\nUpload speed: {} Mbps\nPing time: {} ms".format(download_speed, upload_speed, ping_time)
    bot.send_message(chat_id = 'Your_chat_id', text = message)

if __name__ == '__main__':
    while True:
        download_speed, upload_speed, ping_time = test_speed()
        send_speed(download_speed, upload_speed, ping_time)
        time.sleep(3600)
