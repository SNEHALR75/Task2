from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    expire_date = serializers.DateField(format="%d/%m/%y")
    manufacturing_date = serializers.DateField(format="%d/%m/%y")

    class Meta:
        model = Product
        fields = "__all__"