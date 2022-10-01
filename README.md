# API service that can provide details of a logged-in LinkedIn user's connections

### Installing required packages: 
 	pip install -r requirements.txt
 
### Assign the chromedriver path in the code, linkedIn_scrap_api/internal_code/utils.py : 
	 ```
	# assign the chromedriver path
	CHROMEDRIVER_PATH = r"D:\chromedriver.exe"

	```
### initializing django server: 
 	python manage.py runserver
	
	
## API docs

### Register new user: 
		 ```
		import requests

		url = "http://127.0.0.1:8000/auth/registration/"

		payload = {'username': 'admin2758',
				   'password1': 'pass1232',
				   'password2': 'pass1232',
				   'email': ''}

		response = requests.request("POST", url, data=payload)

		print(response.text)

		```
		
   response = Json file of Token Key 
   
### User Login: 
		 ```
		import requests

		url = "http://127.0.0.1:8000/auth/login/"

		payload = {'username': 'admin2758',
				   'password': 'pass1232'}

		response = requests.request("POST", url, data=payload)

		print(response.text)

		```
		
   response = Json file of Token Key 
   
   
### Scrap connections request:

   Assign token key and linkedIn username and password 
		 ```
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

		```
   response = JSON object object of connections



