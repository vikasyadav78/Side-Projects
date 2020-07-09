from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup


# Getting news from Times of India

times_of_india = requests.get("https://timesofindia.indiatimes.com/coronavirus")
soup = BeautifulSoup(times_of_india.content,'html.parser')
toi_headings = soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footer links

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