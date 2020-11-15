from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen(sys.argv[1])
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(image['src']+'\n')
