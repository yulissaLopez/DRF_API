from rest_framework import serializers
from .models import Product

"""Serializers: Convierten datos entre objetos de Python y formatos como JSON, XML."""

class ProductSerializer(serializers.ModelSerializer):
    # class meta define el modelo que se esta serializando
    class Meta:
        model = Product
        # define los campos que deben incluirse
        fields = [
            'id', 
            'title', 
            'content', 
            'price',
            'sale_price',
            'get_discount'
            ]