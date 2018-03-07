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
        #i=IP()
        proxies_req = Request(url)
        proxies_req.add_header('User-Agent',browser.random)
        return proxies_req
    
ssl._create_default_https_context = ssl._create_unverified_context

browser=UserAgent()
form = cgi.FieldStorage()
id = str(form.getvalue('link'))
link=id
print("Content-type:text/html\r\n\r\n")
print('''
<!doctype html>
<html>
   <head><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=yes">
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

req2=make_request(link)
html2 = urlopen(req2).read().decode('utf8')
soup2=BeautifulSoup(html2,"lxml")
data=soup2.findAll("div",{"class": "nfo"})
data=data[0].encode('utf-8')

movies2 = soup2.findAll("div", {"class": "download"})
a_tag2=movies2[0].findAll("a")
print('<a href={}>Magnet Link</a><hr>'.format(a_tag2[0].attrs["href"]))
print(data.decode('ascii','backslashreplace'))
print('''
   </bodyss>
</html>''')


