from django.shortcuts import get_object_or_404

from Users.models import User

from .models import Products, Cart, CartItem, ProductsMeta
from OnlineCartApp.serializers import ProductSerializer, CartSerializer, CartItemSerializer, ProductMetaSerializer

from rest_framework import generics
from .productpermission import CanAddProduct, CanAddCart


# Create your views here.


class ProductList(generics.ListCreateAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CanAddProduct, ]

    def get_queryset(self):

        userid = self.request.user.id
        user = User.objects.get(id=userid)

        if user.isbusiness:
            queryset = self.queryset.filter(owner=user)
        else:
            queryset = Products.objects.all()

        return queryset


class ProductMetaList(generics.ListCreateAPIView):

    queryset = ProductsMeta.objects.all()
    serializer_class = ProductMetaSerializer


class ProdDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CanAddProduct, ]

    def get_object(self):

        userid = self.request.user.id
        user = User.objects.get(id=userid)
        if user.isbusiness:
            get_object_or_404(Products, id=self.kwargs['pk'], owner=self.request.user)

        if user.isbusiness:
            prod = self.queryset.filter(owner=user, id=self.kwargs['pk']).first()

        else:
            prod = Products.objects.filter(id=self.kwargs['pk']).first()

        return prod


class CartList(generics.ListCreateAPIView):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [CanAddCart, ]


class CartDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [CanAddCart, ]


class CartItemList(generics.ListCreateAPIView):

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [CanAddCart, ]

    def get_queryset(self):

        userid = self.request.user.id
        user = User.objects.get(id=userid)
        cartobj, created = Cart.objects.get_or_create(user=user)
        queryset = self.queryset.filter(cart=cartobj)

        return queryset


class CartItemDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [CanAddCart, ]


