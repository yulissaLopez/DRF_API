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
    # This ia a field that does not exits in the model but its calculated in the get_my_discount method
    my_discount = serializers.SerializerMethodField(read_only=True)
    # class meta define el modelo que se esta serializando
    class Meta:
        model = Product
        # define los campos que deben incluirse
        """
            The my_discount field will be included in the serialized data when you retrieve or list products, but you cannot send a value for my_discount when creating or updating a product, as it is read-only.
        """
        fields = [
            'id', 
            'title', 
            'content', 
            'price',
            'sale_price',
            'my_discount'
            ]

    """
        This method receives the model instance (obj), and it calculates and returns a discount based on the product’s price.
    """
    def get_my_discount(self, obj):
        if obj.price > 100:
            return obj.price * 0.1
        return 0