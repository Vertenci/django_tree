from django.urls import path
from . import views
from .views import MenuItemDetailView

urlpatterns = [
    path('some_page/', views.some_page, name='some_page'),
    path('item/<str:title>/', MenuItemDetailView.as_view(), name='item'),
]
