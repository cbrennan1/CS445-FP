import requests

website = 'http://localhost:8080/bn/api'
def httpstatus(website):
    response = requests.get(website)
    status = response.status_code
    return status
