# https://divar.ir/s/sari/vehicles
from bs4 import BeautifulSoup


def length_tag_a(html):
    soup = BeautifulSoup(html, 'html.parser')
    return len(soup.find_all('a'))

