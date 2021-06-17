# 英語→カタカナ変換機(https://www.sljfaq.org/cgi/e2k_ja.cgi)からスクレイピング
import urllib.request
from bs4 import BeautifulSoup

def english_to_katakana(word):
    url = 'https://www.sljfaq.org/cgi/e2k_ja.cgi'
    url_q = url + '?word=' + word
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    request = urllib.request.Request(url_q, headers=headers)
    html = urllib.request.urlopen(request)
    soup = BeautifulSoup(html, 'html.parser')
    katakana_string = soup.find_all(class_='katakana-string')[0].string.replace('\n', '')

    return katakana_string

word = 'English'

katakana_string = english_to_katakana(word)
print(katakana_string)
