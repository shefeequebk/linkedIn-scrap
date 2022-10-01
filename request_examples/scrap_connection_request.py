import requests

url = "http://127.0.0.1:8000/scrap-connections/"

payload = {'linkedIn_email': '',
           'linkedIn_password': ''}
key = ''  # Token Key


headers = {
    'Authorization': f'Token {key}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
