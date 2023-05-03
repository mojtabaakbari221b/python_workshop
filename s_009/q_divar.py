import requests
import dryscrape
from bs4 import BeautifulSoup
from persian_tools import digits
from requests_html import HTMLSession


# def get_html_from_url(url):
#     r = requests.get(url)
#     return r.text

def get_html_from_url(url):
    session = dryscrape.Session()
    session.visit(url)
    response = session.body()

    return response


# html = get_html_from_url(url="https://divar.ir/s/sari/rent-residential")

# soup = BeautifulSoup(html, 'html.parser')

# for item in soup.find_all(class_='kt-post-card__description') :
#     if not (("ودیعه" in item.text) or ("۰" not in item.text)) :
#         price_with_toman = item.text.replace("اجاره: ", "")
#         price_without_toman = price_with_toman.replace(" تومان", "")
#         price_without_comma = price_without_toman.replace(",", "")
        
#         # print(price_without_comma)
#         eng_price = digits.convert_to_en(price_without_comma)

#         if int(eng_price) <= 4000000 :
#             print("House Founded :))))))))))")