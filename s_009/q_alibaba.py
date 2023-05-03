from q_divar import get_html_from_url
from bs4 import BeautifulSoup


# date_from_user = input("insert your date: ")
date_from_user = "1402-02-15"

html = get_html_from_url(url=f"https://www.alibaba.ir/bus/SRY-MHD?departing={date_from_user}")

soup = BeautifulSoup(html, 'html.parser')




for card in soup.find_all(class_='available-card'):
    print(card.pretiffy())