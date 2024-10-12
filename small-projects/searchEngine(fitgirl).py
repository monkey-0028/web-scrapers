from urllib.request import urlopen
from urllib.error import *
from bs4 import BeautifulSoup
import re

# provide magnet link and also show size info
# search up to 5 pages. then give result...

def generatePattern(gameName):
    r_val = ".* "
    for item in gameName:
        if item != " ":
            r_val += f"({item.upper()}|{item.lower()})"
        else:
            r_val += " "
    r_val += " .*"
    return r_val
def isMatch(p,t):
    if re.match(p,t):
        return True
    return False



gameName = input("Game(fitgirl): ")
link = "https://fitgirl-repacks.site/?s=" + gameName.replace(" ", "+")

pattern = generatePattern(gameName)

try:
    url = urlopen(link)
except URLError as e0:
    print(e0)
except HTTPError as e1:
    print(e1)
else:
    html = BeautifulSoup(url,'html.parser')
    searchList = (html.find_all(lambda tag : (isMatch(pattern,tag.get_text()))and('href' in tag.attrs) ))
    data = dict()
    for item in searchList:
        if item.attrs['href'] not in data:
            data[item.attrs['href']] = item.get_text()

    if data == {}:
        print("\n no game found with this name")
    else:
        print("\n\n")
        for item in data:
            print(f"{data[item]} ::: {item}\n\n")
        
