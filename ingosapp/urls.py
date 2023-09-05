from django.urls import path

from ingosapp.views import home, index, author, foodscience, foodapp


# URLConf
urlpatterns = [
    path('', home),
    path('home/', home),
    path('author/', author),
    path('foodscience/', foodscience),
    path('foodapp/', foodapp),
    path("int:id>", index, name="index"),
]