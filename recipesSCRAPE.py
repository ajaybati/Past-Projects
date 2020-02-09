from urllib.request import Request, urlopen
import urllib.request
from bs4 import BeautifulSoup
searchString="pizza"
real_string = ""
recipe=[]

if " " in searchString:
    compatible = searchString.split(" ")
    lenCount = len(compatible)
    a = 1
    for word in compatible:
        if a == lenCount:
            real_string += word
            break
        real_string += (word + "+")
        a += 1
real_string+=searchString
req = Request("https://www.geniuskitchen.com/search/"+real_string,
              headers={'User-Agent': 'Mozilla/5.0'})
print("https://www.food.com/search/"+real_string)
with urllib.request.urlopen(req) as response:
    page = response.read()
    soup = BeautifulSoup(page, 'html.parser')
    large = soup.find_all('div'.encode("utf-8", "ignore"), 'search-results fdStream')
    for thing in large:
        print(thing)

