from django.urls import path, include
from Users import views
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('signup/', views.CustomerList.as_view()),
    path('registered-users/', views.CustomerList.as_view()),
    path('account/', include('allauth.urls')),
    path('login/', views.CustomerLoginList.as_view()),
    path('login-token/', obtain_auth_token),
    path('signup/<int:pk>/', views.CustomerDetails.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)