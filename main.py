import requests
from bs4 import BeautifulSoup
from email_sender import Email
from decouple import config
import time
import schedule

# You can see the headers of your browser by visiting http://myhttpheader.com/
headers = {
    "Accept-Language": "en-US,en;q=0.9,uk-UA;q=0.8,uk;q=0.7,ru;q=0.6",
    "User-Agent": config("USER"),
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}


def check_price():
    product_url = "https://ua.iherb.com/pr/mount-hagen-organic-fairtrade-instant-coffee-decaffeinated-3-53-oz-100-g/82668"
    iherb_response = requests.get(product_url, headers=headers)
    data = iherb_response.text
    etalon_price = 13.0

    soup = BeautifulSoup(data, "html.parser")
    current_price = float(soup.select(selector="span.price")[1].text.strip()[1:])
    product_name = soup.select(selector="h1#name")[0].text.strip()

    if current_price <= etalon_price:
        email = Email(product_name, current_price)
        email.send()


schedule.every().day.at("02:18").do(check_price)

while True:
    schedule.run_pending()
    time.sleep(1)
