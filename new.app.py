import requests
import json

query = str(input("what type news are you interested in ?"))
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-11-08&sortBy=publishedAt&apiKey=76548e3bb212415681fb41ec775863cf"
r = requests.get(url)
news =json.loads(r.text)
# print(news, type(news))
for allnews in news["articles"]:
    print(allnews["title"])
    print(allnews["description"])
    print("- - - - - - - - - - - -  - - - - - - - - - - -  - - - - - - - - ")

