import requests

url = "http://127.0.0.1:8000/auth/registration/"

payload = {'username': 'admin2758',
           'password1': 'pass1232',
           'password2': 'pass1232',
           'email': ''}

response = requests.request("POST", url, data=payload)

print(response.text)
