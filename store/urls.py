from django.urls import path, include
from rest_framework import routers
from store.views import StoreView

router = routers.DefaultRouter()

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('store/', StoreView.as_view(), name='Store'),
    path('store/<int:pk>/', StoreView.as_view(), name='store-detail'),
]
