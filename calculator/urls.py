from django.urls import path
from . import views

urlpatterns = [
    path('', views.FoodCalculateView.as_view(),  name="calculate")
    # path('', views.CalculatorView.as_view(), name='example'),
    # path('calculator/', views.calculator_view, name='calculator_view'),
    # Define your URL patterns here
]