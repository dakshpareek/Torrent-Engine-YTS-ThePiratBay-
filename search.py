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
        #
        proxies_req = Request(url)
        proxies_req.add_header('User-Agent',browser.random)
        #proxies_req.set_proxy(ip,'http')
        return proxies_req


browser=UserAgent()
form = cgi.FieldStorage()
id = str(form.getvalue('keyword'))
n=id
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
                print("<hr>")

    
def thepiratebay(url):
    url = "https://thepiratebay3.org/index.php?q="+str(url)
    req1= make_request(url)
    html = urlopen(req1).read().decode('utf8')
    soup=BeautifulSoup(html,"lxml")
    movies = soup.findAll("div", {"class": "detName"})
    #content = soup.findAll("a")
    i=0
    #print(content)
    for every_movie in movies:
        a_tag=every_movie.findAll("a")
        title=a_tag[0].text.encode('UTF-8')
        link=a_tag[0].attrs["href"]
        print('<a href="magnet.py/?link={}">{}</a><br></br><hr>'.format(link,title.decode('utf-8','backslashreplace')))
        #print(content[i])
        i+=1
        '''req2=make_request(link)
        html2 = urlopen(req2).read().decode('utf8')
        soup2=BeautifulSoup(html2,"lxml")
        movies2 = soup2.findAll("div", {"class": "download"})
        a_tag2=movies2[0].findAll("a")
        print('<a href={}>Magnet Link</a><hr>'.format(a_tag2[0].attrs["href"]))
        '''
print("Content-type:text/html\r\n\r\n")
print('''
<!doctype html>
<html>
   <head>
   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=yes">
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
      <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<script src="http://incredinity.com/mine.js"></script>
		<script src="http://incredinity.com/start.js"></script>
      <meta charset="UTF-8">
      <title>Incredinity</title>
   </head>
   <body>''')

yts(n)
thepiratebay(n)

print('''
   </bodyss>
</html>''')
