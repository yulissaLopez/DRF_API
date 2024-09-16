from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer


@api_view (["GET"]) # defino que metodos http quiero permitir GET, POST ..
def api_home(request):
    """ DRF API View """
    """
        Product.objects.all() -> que trae todos los registros del modelo
        order.by("?") -> los ordena de forma aleatoria con el argumento ?
        first() -> devuelve el primer objeto
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}

    """
        ProductSerializer(instance) crea un serializer para la instancia
        del modelo

        .data Obtinen la reperesntacion serializada de la instancia en forma de diccionario
    """
    if instance:
        data = ProductSerializer(instance).data
        print(data)
    return Response(data)

@api_view(["POST"]) # Esta view solo permite metodos post
def api_add(request):
    # request.data es un diccionario que contieme los datos enviados en la solicitud, los cuales provienen del cuerpo de la solictud

    # Al pasarlos a ProductSerializer le estoy diciendo que tome esos datos y los deserialice y valide para crear un objeto product
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid(): # Verifica si los datos son validos
        instance = serializer.save() # Guarda el nuevo objeto Product en la BD
        print(instance)
        data = serializer.data
        return Response(data)
    else: 
        print(serializer.errors) # Si no son válidos, devuelve los errores

    #1:20:32
