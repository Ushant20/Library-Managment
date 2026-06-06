# import requests
# import os

# ACCESS_TOKEN = ("EAAPexbotiaABRkfh0N2C1Y8chrZAig8l1aNGDPwQ5IlFhFcF4rpvIoOJZAYJBKQII1w6j49l3JRzLbdZCS0FnL6nMhLl1IZCNh0M8NgZBLOJdGMBDJdvDwk3WBDh15sZCnuYQx7GNZCdkaFHVAWAFsgDrQivgZBoMrkxgkamjSWFURwxASFxkZBZA9ndYNJU02YrAKEGLKsZBMaGeNOz8Fnv23foF5Urmkh6ZAK5m9Ja20bHGFIkWHzo0naclcX807EeHGgtJCZA07UCEtwToXd20RrZAA")
# PHONE_NUMBER_ID =("1063466313526464")


# def send_whatsapp_message(phone, message):

#     print("Sending WhatsApp to:", phone)

#     url = f"https://graph.facebook.com/v25.0/{PHONE_NUMBER_ID}/messages"

#     headers = {
#         "Authorization": f"Bearer {ACCESS_TOKEN}",
#         "Content-Type": "application/json",
#     }

#     payload = {
#         "messaging_product": "whatsapp",
#         "to": phone,
#         "type": "text",
#         "text": {
#             "body": message
#         }
#     }

#     response = requests.post(
#         url,
#         headers=headers,
#         json=payload
#     )

#     print("Status:", response.status_code)
#     print("Response:", response.text)

#     return response.json()