from rest_framework import serializers
from .models import Product

"""Serializers: Convierten datos entre objetos de Python y formatos como JSON, XML."""
"""
    Serialización: Convertir datos de modelos a formatos que puedan ser enviados como respuestas JSON, XML, etc.
    Deserialización: Tomar datos (usualmente en formato JSON) y convertirlos en instancias de modelos u otros tipos de datos en Python.
"""

"""
    ProductSerializer actúa como una clase que sabe cómo convertir los datos JSON a una instancia del modelo Product, y también cómo validar esos datos.
"""
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