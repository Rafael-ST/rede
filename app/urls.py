from django.urls import path
from app import views
from .views import HelloWorld, UserCreate, BairroListView, LiderDeEquipeCreateView, LiderListView, AmigoListView, AmigoListViewAll
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.index, name='index'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('hello/', HelloWorld.as_view(), name='hello-world'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreate.as_view(), name='user_register'),
    path('bairros/', BairroListView.as_view(), name='bairro-list'),
    path('lideresview/', LiderListView.as_view(), name='lideres-list'),
    path('lideres/', LiderDeEquipeCreateView.as_view(), name='lider-create'),
    path('amigos/', AmigoListView.as_view(), name='amigo-list'),
    path('amigos_all/', AmigoListViewAll.as_view(), name='amigos-all'),
    path('incluir_lider', views.incluir_lider, name='incluir_lider'),
    path('loginoperador', views.loginoperador, name='loginoperador'),

    path('contatos', views.contatos, name='contatos'),
]