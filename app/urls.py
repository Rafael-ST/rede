from django.urls import path
from .views import HelloWorld, UserCreate, BairroListView, LiderDeEquipeCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('hello/', HelloWorld.as_view(), name='hello-world'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreate.as_view(), name='user_register'),
    path('bairros/', BairroListView.as_view(), name='bairro-list'),
    path('lideres/', LiderDeEquipeCreateView.as_view(), name='lider-create'),
]