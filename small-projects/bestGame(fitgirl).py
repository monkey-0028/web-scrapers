from urllib.request import urlopen
from urllib.error import *
import re
from bs4 import BeautifulSoup

try:
    url = urlopen("https://fitgirl-repacks.site/?s=god")
except HTTPError as e1:
    print(e1)
except URLError as e2:
    print(e2)
else:
    html = BeautifulSoup(url,'html.parser')
    box = html.find_all('div',{'class':'jetpack_top_posts_widget'})
    print(box[0].h2.get_text(),"\n")
    iter = 1
    for item in box[0].find_all('img'):
        print(f"{iter}. {item.attrs['alt']} : {item.attrs['src']}")
        iter += 1
