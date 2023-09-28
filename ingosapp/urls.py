from django.urls import path
from . import views
# from ingosapp.views import home, author, foodscience, foodapp

app_name = "ingosapp"
# URLConf
urlpatterns = [
    # path('', home),
    # path('home/', home),
    # path('author/', author),
    # path('foodscience/', foodscience),
    # path('foodapp/', foodapp),
    path("", views.IndexView.as_view(), name="home"),
    path("food_science", views.FoodScienceView.as_view(), name="food"),
    path("food_app", views.FoodAppView.as_view(), name="food"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
    path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
    path('blog/', views.BlogView.as_view(), name="blogs"),
    # path("int:id>", index, name="index"),
]