import requests

response = requests.get('http://localhost:8080/bn/api')
httpStatus = response.status_code