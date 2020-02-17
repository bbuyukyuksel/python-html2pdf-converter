import pdfkit  #https://wkhtmltopdf.org/downloads.html
import requests
from bs4 import BeautifulSoup
import os

r = requests.get('https://github.com/necatiergin/Cplusplus_Ders_Notlari')
source = BeautifulSoup(r.content,"html.parser")
links = source.find_all("a", attrs={"class":"js-navigation-open"})

links = list(filter(lambda x: x["href"] != '', links))

PREFIX = '.'
fpath = os.path.join(PREFIX, "C++ Ders Notları")
if not os.path.isdir(fpath):
    os.makedirs(fpath, exist_ok=True)
for link in links:
    print(fpath ,link.text.split('.')[0], sep='/')
    pdfkit.from_url("https://github.com{}".format(link["href"]),'{}/{}.pdf'.format(fpath ,link.text.split('.')[0])) 
