import pdfkit  #https://wkhtmltopdf.org/downloads.html
import requests
from bs4 import BeautifulSoup
import os

PREFIX = '.'
fpath = os.path.join(PREFIX, "C++ Ders Notları")
if(not os.path.exists(fpath)):
    print("C++ ders notları indiriliyor...")
    
    if not os.path.isdir(fpath):
        os.makedirs(fpath, exist_ok=True)
    r = requests.get('https://github.com/necatiergin/Cplusplus_Ders_Notlari')
    source = BeautifulSoup(r.content,"html.parser")
    links = source.find_all("a", attrs={"class":"js-navigation-open"})
    links = list(filter(lambda x: x["href"] != '', links))

    for link in links:
        print(fpath ,link.text.split('.')[0], sep='/')
        pdfkit.from_url("https://github.com{}".format(link["href"]),'{}/{}.pdf'.format(fpath ,link.text.split('.')[0])) 


fpath = os.path.join(PREFIX, "C++ Ödevler")
if(not os.path.exists(fpath)):
    print("C++ ödevleri indiriliyor...")
    
    if not os.path.isdir(fpath):
        os.makedirs(fpath, exist_ok=True)
    r = requests.get('https://github.com/necatiergin/cpp_kursu_odevleri')
    source = BeautifulSoup(r.content,"html.parser")
    dir_links = source.find_all("a", attrs={"class":"js-navigation-open"})
    dir_links = list(filter(lambda x: x["href"] != '', dir_links))

    for dir_link in dir_links:
        tpath = os.path.join(fpath, dir_link.text)
        if not os.path.isdir(tpath):
            os.makedirs(tpath, exist_ok=True)

        r = requests.get('https://github.com{}'.format(dir_link["href"]))
        source = BeautifulSoup(r.content,"html.parser")
        content_links = source.find_all("a", attrs={"class":"js-navigation-open"})
        content_links = list(filter(lambda x: x["href"] != '' and not x.has_key("rel"), content_links))
        for link in content_links:
            print(tpath ,link.text.split('.')[0], sep='/')
            pdfkit.from_url("https://github.com{}".format(link["href"]),'{}/{}.pdf'.format(tpath ,link.text.split('.')[0])) 

