import cgi, cgitb
from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import json,random
import time
from get_ip import IP
from fake_useragent import UserAgent
import cgi, cgitb

def make_request(url):
        proxies_req = Request(url)
        proxies_req.add_header('User-Agent',browser.random)
        proxies_req.set_proxy(ip,'http')
        return proxies_req

i=IP()
browser,ip=i.ip()

n=input("Enter Keyword")
n=n.replace(" ","+")

ssl._create_default_https_context = ssl._create_unverified_context

def yts(url):
        url = "https://yts.am/browse-movies/{}/all/all/0/latest".format(url)
        req1= make_request(url)
        html = urlopen(req1).read().decode('utf8')
        soup=BeautifulSoup(html,"lxml")
        movies = soup.findAll("a", {"class": "browse-movie-link"})
        all_data=[]
        i=0
        for every_movie in movies:
                title=every_movie.findAll("img")
                title=title[0].attrs['alt']
                link=every_movie.attrs['href']
                print('''<b>{}</b></br>'''.format(title))
                req2=make_request(link)
                html2 = urlopen(req2).read().decode('utf8')
                soup2=BeautifulSoup(html2,"lxml")
                movies1 = soup2.findAll("p", {"class": "hidden-xs hidden-sm"})
                movies1 = movies1[0].findAll("a")
                for every_movie1 in movies1:
                    print('<a href={}>{}</a>'.format(every_movie1.attrs['href'],every_movie1.text))

print(ip)
yts(n)

