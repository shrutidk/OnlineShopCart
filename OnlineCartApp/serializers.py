from rest_framework import serializers
from Users.models import User
from .models import Products, Cart, CartItem, ProductsMeta


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'quantity', ]

    def validate(self, data):

        if data['quantity'] < 0:
            raise serializers.ValidationError("Quantity cannot be negative")
        if data['quantity'] is None:
            raise serializers.ValidationError("Quantity cannot be blank")
        if data['price'] < 0:
            raise serializers.ValidationError("Price cannot be negative")

        if data['name'] is None:
            raise serializers.ValidationError("Please Enter valid Product name")
        return data

    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        user_id = self.context['request'].user.id
        user = User.objects.get(id=user_id)

        prodobj = Products.objects.create(productowner=user, **validated_data)
        return prodobj

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.title = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.availquantity)

        instance.save()
        return instance


class ProductMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsMeta
        fields = ['id', 'name', 'price', 'quantity', ]

    def create(self, validated_data):
        return ProductsMeta.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.title = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)

        instance.save()
        return instance


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id', 'cartuser', 'createddate']

    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        return Cart.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.cartuser = validated_data.get('cartuser', instance.cartuser)
        instance.createddate = validated_data.get('createddate', instance.createddate)

        instance.save()
        return instance


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['id', 'quantity', 'product', 'cart']

    def validate(self, data):
        if data['product'] is None:
            raise serializers.ValidationError("Enter a valid product")

        if data['quantity'] < 0:
            raise serializers.ValidationError("Enter a valid positive value as quantity")

        if data['quantity'] == 0:
            raise serializers.ValidationError("Enter a non-zero value as Quantity")

        return data

    def to_internal_value(self, data):
        if data.get('quantity') == '':
            data['quantity'] = 1

        if data.get('quantity') is None:
            data['quantity'] = 1

        return super(CartItemSerializer, self).to_internal_value(data)

    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """

        user_id = self.context['request'].user.id
        user = User.objects.get(id=user_id)
        cartobj, created = Cart.objects.get_or_create(cartuser=user)

        prod_id = validated_data['product']
        qnt = validated_data['quantity']

        if qnt > prod_id.quantity:
            raise serializers.ValidationError({"errors": "Selected quantity not available"})

        #added
        # name = prod_id.name
        # price = prod_id.price
        # qnt = prod_id.availquantity
        #
        # prodmetadata={'name':name,'price': price,'availquantity' : qnt}
        #
        # prodmetaser = ProductMetaSerializer(data = prodmetadata)
        #
        # if prodmetaser.is_valid():
        #     prodmetaobj = prodmetaser.save()

        cartitems = CartItem.objects.create(cart=cartobj, **validated_data)

        # print(CartItemSerializer(instance=cartitems).data)

        return cartitems

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.product = validated_data.get('product', instance.product)

        instance.save()
        return instance
