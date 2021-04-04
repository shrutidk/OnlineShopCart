
from .orderpermission import CanOrder
from .models import Orders
from Product.serializers import OrderSerializer
from rest_framework import generics

# Create your views here.


class OrderList(generics.ListCreateAPIView):

    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CanOrder,]

    def get_queryset(self):
        userid = self.request.user.id
        queryset = self.queryset.filter(orderuser=userid)

        return queryset


class OrderDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CanOrder, ]
