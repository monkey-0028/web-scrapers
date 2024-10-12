from urllib.request import urlopen
from urllib.error import *
from bs4 import BeautifulSoup
import re

p = ".*(G|g)od (O|o)f (W|w)ar.*"
href_p = ".* href.*"

def match(p,t):
    if re.match(p,t):
        return True
    else:
        return False


try:
    url = urlopen("https://fitgirl-repacks.site/?s=god+of+war")
except URLError as e1:
    print("inCorrect Link\n\n")
    print(e1)
except HTTPError as e2:
    print(e2)
else:
    html = BeautifulSoup(url,'html.parser')
    tagList = html.find_all(lambda tag : match(p,tag.get_text()))
    gameList = dict()
    for item in tagList:
        try:
            if 'href' in item.attrs:
                if item.attrs['href'] in gameList:
                    pass
                else:
                    gameList[item.attrs['href']] = item.get_text()
        except:
            pass
    for item in gameList:
        print(f"{gameList[item]} ::: {item}\n\n")