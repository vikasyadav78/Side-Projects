from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup


# Getting news from Times of India

times_of_india = requests.get("https://timesofindia.indiatimes.com/india/coronavirus-live-updates-india-will-play-a-leading-role-in-global-revival-pm-modi-says/liveblog/76843875.cms")
soup = BeautifulSoup(times_of_india.content,'html.parser')
toi_headings = soup.find_all("div",{"class":"_1KydD"})

toi_headings

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



#Getting news from Hindustan times

hindustan_times= requests.get("https://www.hindustantimes.com/topic/coronavirus")
soup = BeautifulSoup(hindustan_times.content, 'html.parser')

ht_headings = soup.findAll("div", {"class": "headingfour"})
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ht_news': ht_news})