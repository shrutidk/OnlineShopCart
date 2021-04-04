from django.contrib import admin
from django.urls import path
from Product import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    path('order/',views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetails.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)