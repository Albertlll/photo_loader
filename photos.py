import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import common
import requests
import os
root_dir = input("Корневая папка: ")
street_dir = input("Название уличной папки: ")

pho = []
with open("photos_names.txt", mode="rt", encoding="UTF-8") as file:
    lines = file.readlines()
    for i in lines:
        pho.append(i.strip())

print(pho)


yet_pho = []
yet_photo_dir = list(os.walk("images"))

yet_pho.extend(yet_photo_dir[1][2])
yet_pho.extend(yet_photo_dir[2][2])

for i in pho:
    if i[-1] == "у":
        link = f"{root_dir}/{street_dir}/{i[:8].strip()}.jpg"
        print(link)
        with requests.session() as session:
            session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
            im = requests.get(link)
            out = open(f"images/street/{i[:8]}.jpg", "wb")
            out.write(im.content)
            out.close()
            print(i)
    elif i[-1] == "с":

        link = f"{root_dir}/{i[:8].strip()}.jpg"
        with requests.session() as session:
            session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
            im = requests.get(link)
            out = open(f"images/house/{i[:8]}.jpg", "wb")
            out.write(im.content)
            out.close()
            print(i)


