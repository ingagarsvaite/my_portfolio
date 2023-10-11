from django.urls import path
from . import views

urlpatterns = [
    path('', views.FoodCalculateView.as_view(),  name="calculate")
]