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
        #1:14:44
    return Response(data)
    
