import requests

key = 'AIzaSyCt-MlxnuCfWJLeLAqzxg3qqQw64qQ20bI'

url = 'https://www.googleapis.com/youtube/v3/channels'

def getChannel1():
    request = requests.get(url)
    show = print(request.content)
    show

getChannel1()