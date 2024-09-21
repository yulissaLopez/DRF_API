import requests

# endpoint = "http://localhost:8000/api/products/2/"

# get_response = requests.get(endpoint)
# print(get_response.json())

endpoint = "http://localhost:8000/api/products/"
data = {
    'title' : "Create view",
    'content' : "content",
    'price' : 10.5
}

get_response = requests.post(endpoint, data)
print(get_response.json())