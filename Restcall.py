import requests #imported the external requests module for Python using PIP install requests command
from requests.exceptions import HTTPError #import a paticular module from the parent module

try: 
    response = requests.get('http://httpbin.org/get')
    response.raise_for_status()
    jsonResponse=response.json()
    print('entire JSON response')
    print(jsonResponse)

except HTTPError as http_err:
    print(f'http error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

print(jsonResponse.items())

print('Key value pairs from json response')
for key, value in jsonResponse.items():
    print(key, ":",value)
print("definite key from JSON object")
print("URL is: ")
print(jsonResponse["url"])
print("Nested JSON object value")
print("value of Host is")
print(jsonResponse["headers"]["Host"])