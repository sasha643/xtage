"""
URL configuration for explorer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from users.views import RegisterView
from places.views import SearchPlacesView, SavePlaceView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import *
from places.views import SavePlaceView
from django.views.decorators.csrf import csrf_exempt
from places.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path("api/save-place/", SavePlaceView.as_view(), name="save_place"),
    path("api/search-place/", SearchPlacesView.as_view(), name="search_place"),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)))
]
