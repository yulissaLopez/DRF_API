# generics es una clase que proporciona una funcionalidad comun y flexible para manejar diferentes tipos de peticiones HTTP (GET, POST, PUT, DELETE)
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# La clase CreateAPIView es para read-only end points para traer una unica instancia de un modelo (puede ser por pk)
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # serializer se refiere al Productserializer que ha registrado los datos de entrada
    # Contiene los datos que el cliente ha enviado
    def perform_create(self, serializer):
        # validate_data es un diccionario que contiene todos los datos que han sido validados
        title = serializer.validate_data.get("title")
        # si el content no esta definido se le asigna None
        content = serializer.validate_data.get('content') or None

        if content is None:
            content = title
        # Aqui se guarda el nuevo objeto en la base de datos, pasandole el content que hemos determinado
        serializer.save(content = content)

product_create_view = ProductCreateAPIView.as_view()

# La clase RetrieveAPIView es para read-only end points para traer una unica instancia de un modelo (puede ser por pk)
# Maneja un metodo GET
class ProductDetailAPIView(generics.RetrieveAPIView):
    # Conjunto de datos del modelo donde opera la lista
    queryset = Product.objects.all()
    # Como se vab a convertir los objetos a JSON
    serializer_class = ProductSerializer
    #lookup_field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()


class ProductCreateListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # serializer se refiere al Productserializer que ha registrado los datos de entrada
    # Contiene los datos que el cliente ha enviado
    def perform_create(self, serializer):
        # validate_data es un diccionario que contiene todos los datos que han sido validados
        title = serializer.validated_data.get("title")
        # si el content no esta definido se le asigna None
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title
        # Aqui se guarda el nuevo objeto en la base de datos, pasandole el content que hemos determinado
        serializer.save(content = content)

product_list_create_view = ProductCreateListCreateAPIView.as_view()

