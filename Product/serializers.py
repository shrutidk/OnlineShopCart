from rest_framework import serializers
#from django.contproductrib.auth.models import User
from OnlineCartApp.serializers import ProductSerializer
from .models import Orders
from OnlineCartApp.models import Products


class OrderSerializer(serializers.ModelSerializer):
    product= ProductSerializer()

    class Meta:
        model = Orders
        #fields = '__all__'
        fields = ['id','product','totalprice','orderquantity']
        #exclude=['product.price','product.quantity']

    # def validate(self, data):
    #     if data['quantity'] < 0:
    #         raise serializers.ValidationError("Quantity cannot be negative")
    #     if data['quantity'] == 0:
    #         raise serializers.ValidationError("Quantity cannot be zero")
    #     if data['quantity'] > Products.objects.get(name=self.product).quantity:
    #         raise serializers.ValidationError("Entered quantity exceeds Available quantity")

    def create(self, validated_data):
        """
        Create and return a new `Order` instance, given the validated data.
        """
        product_data = validated_data.pop('product')
        order = Orders.objects.create(**validated_data)
        Products.objects.create(user=order, **product_data)
        return order
        #return Orders.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Order` instance, given the validated data.
        """
        instance.product = validated_data.get('product', instance.product)
        instance.totalprice = validated_data.get('totalprice', instance.totalprice)
        instance.quantity = validated_data.get('quantity', instance.quantity)

        instance.save()
        return instance



