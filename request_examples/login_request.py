import requests

url = "http://127.0.0.1:8000/auth/login/"

payload = {'username': 'admin2758',
           'password': 'pass1232'}

response = requests.request("POST", url, data=payload)

print(response.text)
