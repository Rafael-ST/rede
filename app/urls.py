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
    path('logout', views.logout, name='logout'),
    path('amigos_lider/<int:pk>', views.amigos_lider, name='amigos_lider'),
    path('amigos', views.amigos, name='amigos'),
    path('contatos', views.contatos, name='contatos'),
    path('add_lider', views.add_lider, name='add_lider'),
    path('add_amigo', views.add_amigo, name='add_amigo'),
    path('excluir_amigo/<int:pk>', views.excluir_amigo, name='excluir_amigo'),
    path('excluir_lider/<int:pk>', views.excluir_lider, name='excluir_lider'),
    path('lider_view/<int:pk>', views.lider_view, name='lider_view'),
    path('atualizar_lider/<int:pk>', views.atualizar_lider, name='atualizar_lider'),
]