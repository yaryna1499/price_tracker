# This class is responsible for sending email to myself using this API https://www.mailjet.com/
from mailjet_rest import Client
from decouple import config


class Email:
    def __init__(self, product_name, current_price):
        self.product_name = product_name
        self.current_price = current_price
        self.api_key = config('KEY')
        self.api_secret = config('SECRET')
        self.mailjet = Client(auth=(self.api_key, self.api_secret), version='v3.1')
        self.data = {
            'Messages': [
                {
                    "From": {
                        "Email": "yyyzzz9914@gmail.com",
                        "Name": "Yaryna"
                    },
                    "To": [
                        {
                            "Email": "yyyzzz9914@gmail.com",
                            "Name": "Yaryna"
                        }
                    ],
                    "Subject": "Product price change!",
                    "TextPart": f"{product_name} is now ${current_price}! Hurry up to buy it!",
                }
            ]
        }

    def send(self):
        result = self.mailjet.send.create(data=self.data)
        print(result.status_code)
        print(result.json())

# # test
# email = Email()
# email.send()
