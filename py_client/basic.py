import requests

#endpoint = "https://httpbin.org/200/"
#endpoint = "https://httpbin.org/anything"
#endpoint = "http://localhost:8000/api/"
endpoint = "http://localhost:8000/api/add"

#get_response = requests.get(endpoint, params = {"abc" : 123}, json = { "saludo" : "Hola"}) #HTTP REQUEST
get_response = requests.post(endpoint, json={"title" : "Hello", "content" : "World", "price" : 100.00 } )
#print(get_response.text) # print the raw text response

print(get_response.status_code)  # Verificar el código de estado HTTP
#print(get_response.text)
#JavaScript Object Notation (JSON) - pyhton Dict
print(get_response.json())

#Satus Code
#print(get_response.status_code)

#print(get_response.url)