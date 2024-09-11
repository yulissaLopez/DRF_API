import requests

#endpoint = "https://httpbin.org/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params = {"abc" : 123}, json = { "saludo" : "Hola"}) #HTTP REQUEST
#print(get_response.text) # print the raw text response

#JavaScript Object Notation (JSON) - pyhton Dict
#print(get_response.json())

#Satus Code
#print(get_response.status_code)

print(get_response.url)