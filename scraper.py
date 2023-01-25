import random
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from config import (
    URL_WISE, FROM_WISE, TO_WISE, AMOUNT_WISE,
    URL_XE, FROM_XE, TO_XE, AMOUNT_XE,
    TAG_WISE, CLASS_WISE, 
    TAG_XE, CLASS_XE, 
    PROXY_IPS
    )

def get_exchange_rate_wise(amount: float, from_currency: str, to_currency: str):
    
    # Set the url for scraping
    url = URL_WISE + FROM_WISE + from_currency + TO_WISE + to_currency + AMOUNT_WISE + str(amount)

   # Prepare the page to scrap
    page = requests.get(url, proxies=get_proxy(), headers=get_agent())
    soup = BeautifulSoup(page.content, "html.parser")

    rate = soup.find(TAG_WISE, class_ = CLASS_WISE)

    if rate:
        rate = rate.get_text()
        rate_data = {
            "url": url.split("/")[2],
            "amount": amount,
            "from": from_currency,
            "to": to_currency,
            "rate": rate
        }
    return rate_data

def get_exchange_rate_xe(amount: float, from_currency: str, to_currency: str):

    # Set url of xe.com for scraping
    url = URL_XE + AMOUNT_XE + str(amount) + FROM_XE + from_currency + TO_XE + to_currency
 
   # Prepare the page to scrap
    page = requests.get(url, proxies=get_proxy(), headers=get_agent())
    soup = BeautifulSoup(page.content, "html.parser")

    rate = soup.find(TAG_XE, class_ = CLASS_XE)

    if rate:
        rate = rate.get_text()
        rate = rate.split(" ")[3] 
        rate_data = {
            "url": url.split("/")[2],
            "amount": amount,
            "from": from_currency,
            "to": to_currency,
            "rate": rate
        }
    return rate_data

def get_proxy():
    # Random proxy IP
    proxy = {"http": random.choice(PROXY_IPS)}
    return proxy

def get_agent():
    # Randon User Agent
    user_agent = {"User-Agent": UserAgent().random}
    return user_agent
