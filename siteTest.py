import sys
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

   
try:
    html = urlopen(sys.argv[1])
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found!")
else:
    print("Seite gefunden")    
 