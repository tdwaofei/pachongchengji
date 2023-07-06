# coding: utf-8
# File: downloadcaptcha.py
import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    url = 'http://query1.bjeea.cn/captcha'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')
    for img in img_tags:
        data_url = img['data-url']
        try:
            print(data_url)
        except UnicodeDecodeError:
            print("Unable to decode the data URL")
