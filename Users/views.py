
from rest_framework import status, generics
from rest_framework.response import Response

from .models import User
from Users.serializers import UserSerializer, LoginSerializer
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token

# Create your views here.


class CustomerList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerLoginList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):

        credentials = {
            "username":  request.data.get("username", ""),
            "password": request.data.get("password", ""),
        }

        user = authenticate(**credentials)

        if user is not None:
            login(request, user)
            token = Token.objects.get(user=user).key
            return Response({"token": token}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)





