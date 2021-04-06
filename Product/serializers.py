from rest_framework import serializers
from OnlineCartApp.serializers import ProductMetaSerializer
from Users.models import User
from .models import Orders, OrderItem
from OnlineCartApp.models import Products, CartItem, Cart


class OrderSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    def get_products(self, obj):

        order_obj = OrderItem.objects.filter(order=obj)
        products = [item.product for item in list(order_obj)]
        orderprod = ProductMetaSerializer(products, many=True).data

        return orderprod

    class Meta:

        model = Orders
        fields = ['id', 'subtotal', 'tax', 'total', 'products']

    def create(self, validated_data):
        """
        Create and return a new `Order` instance, given the validated data.
        """
        user_id = self.context['request'].user.id
        user = User.objects.get(id=user_id)

        cartobj = Cart.objects.get(user=user_id)

        cartitemobj = CartItem.objects.all().filter(cart=cartobj)

        subtotal = 0

        for cartitem in cartitemobj.iterator():

            prod_id = cartitem.product
            print(prod_id)
            print(prod_id.id)
            prod = Products.objects.get(id=prod_id.id)

            if cartitem.quantity > prod.quantity:
                raise serializers.ValidationError({"errors": "Selected quantity in cart not available now"})

            subtotal = subtotal + cartitem.product.price * cartitem.quantity

        tax = subtotal*(8/100)
        total = subtotal+tax

        order_data = {'subtotal': subtotal, 'tax': tax, 'total': total, 'user': user}
        orderserializer = OrderSerializer(data=order_data)

        orderobj = Orders.objects.create(**order_data)

        for cartitem in cartitemobj.iterator():
            name = cartitem.product.name
            price = cartitem.product.price
            qnt = cartitem.quantity

            prodmetadata = {'name': name, 'price': price, 'quantity': qnt}

            prodmetaser = ProductMetaSerializer(data=prodmetadata)

            if prodmetaser.is_valid():
                prodmetaobj = prodmetaser.save()

            orderitemdata = {'quantity': qnt, 'price': price, 'order': orderobj, 'product': prodmetaobj}
            OrderItem.objects.create(**orderitemdata)

        '#deduct order quantity from products'

        for cartitem in cartitemobj.iterator():
            prod_id = cartitem.product.id
            prodobj = Products.objects.get(id=prod_id)
            prodobj.quantity = prodobj.quantity - cartitem.quantity
            prodobj.save()

        '#make cart empty'
        cartitemobj.delete()

        return orderobj

    def update(self, instance, validated_data):
        """
        Update and return an existing `Order` instance, given the validated data.
        """
        instance.subtotal = validated_data.get('subtotal', instance.subtotal)
        instance.tax = validated_data.get('tax', instance.tax)
        instance.total = validated_data.get('total', instance.total)

        instance.save()
        return instance



