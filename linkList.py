from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

html = urlopen(sys.argv[1])
bsObj = BeautifulSoup(html)
for link in bsObj.findAll("a"):
  if 'href' in link.attrs:
    print(link.attrs['href'])
