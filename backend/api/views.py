import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from products.models import Product

def api_home(request):
    body = request.body #Devuelve una cadena de bytes
    data = {}
    try:
        data = json.loads(body) # Covertir cadena de texto en diccionario 
    except:
        pass

    print(request.GET)

    return JsonResponse(data)

# ---- Without Django REST FRMEWORK
# def api_home(request, *args, **Kwargs ):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])

#     # if model_data:
#     #     data['id'] = model_data.id
#     #     data['title'] = model_data.title
#     #     data['content'] = model_data.content
#     #     data['price'] = model_data.price
#     #     #serialization
#     #     # model instance
#     #     # turn into a python dict
#     #     # resturn Json to my client
#     return JsonResponse(data)

#     # # request -> HttpRequest -> Django
#     # body = request.body # byte string of Json data
#     # data = {}
#     # try:
#     #     # Convierte una cadena en formato json a un objeto de python
#     #     data = json.loads(body)
#     # except:
#     #     pass

#     # # Acceder al content type
#     # data['content_type'] = request.content_type
#     # # Acceder a los headers
#     # data['headers'] = dict(request.headers)
#     # # Acceder a los url query params
#     # data['params'] = dict(request.GET)

    
#     # # method = request.method
#     # # print(method)
#     # # print the keys od the dictionary
#     # #print(data.keys())
    
#     # return JsonResponse(data)