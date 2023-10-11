from django.urls import path
from . import views
from .views import DownloadCVView



app_name = "ingosapp"
# URLConf
urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path('download-cv/', DownloadCVView.as_view(), name='download_cv'),
    path("food_science", views.FoodScienceView.as_view(), name="foodscience"),
    path('contact/', views.ContactView.as_view(), name="contact")
]