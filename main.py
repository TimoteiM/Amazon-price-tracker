import requests, lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/Amazon-Basics-Lightweight-Microfiber-Comforter/dp/B01947QSK0/ref=sr_1_1_sspa?c=ts&keywords=Bedding%2BComforter%2BSets&qid=1660042828&s=bedbath&sr=1-1-spons&ts_id=14053321&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQzlHWU4zUEtRTk1EJmVuY3J5cHRlZElkPUEwNDg2MDMyM0xDTFVUQTRFTUFCWSZlbmNyeXB0ZWRBZElkPUEwMDg1ODQ0SjhIVVhRM0oxVjUmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1"

header = {

    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
BUY_PRICE = 60
my_email = "moscaliuc_timotei@yahoo.com"

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

title = soup.find(id="productTitle").get_text()

price = soup.find(id="corePriceDisplay_desktop_feature_div").get_text()
price = price[0:9]
price = float(price.split('$')[1])

if price < BUY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com", port=534) as connection:
        connection.starttls()
        connection.login(user=my_email, password="secret")
        connection.sendmail(from_addr=my_email,
                            to_addrs="moscaliuctimotei@gmail.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{message}")


















