import requests

url = "https://gate.whapi.cloud/messages/text?token=haTYU7n4fIryOWHkAqUsqz0xKHsOg1Oh"

payload = {
    "typing_time": 2,
    "to": "62895392349444@s.whatsapp.net",
    "body": "Pesan ini dikirim melalui python dengan whapi, flask."
}

headers = {
    "accept":"application/json",
    "content-type":"application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
