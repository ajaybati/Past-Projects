from urllib.request import Request, urlopen
import urllib.request
from bs4 import BeautifulSoup

garb=[]
good=[]
req = Request("https://www.geekslop.com/2014/comic-book-characters-superheroes-villains-real-names-true-identities",
                  headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    page = response.read()
    soup = BeautifulSoup(page, 'html.parser')
    partial=soup.find("tbody")
    new=soup.find_all("tr")
    for things in new:
        garb.append(things.text)
    for thing in garb:
        if "\n" in thing:
            index=thing.split("\n")
            
            good.append(index[0])
    print(good)
            

            
        
        
