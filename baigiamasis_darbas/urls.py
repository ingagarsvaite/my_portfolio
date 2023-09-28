"""
URL configuration for baigiamasis_darbas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# # from postit_api import urls
# from django.views.generic import RedirectView
# # import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ingosapp.urls')),
    # path('', include('ingosapp.urls'), namespace="ingosapp"),
    path('api/', include('postit_api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('notebooks/', include('notebooks.urls')),
    path('food_app/', include("calculator.urls"))
    # path("", RedirectView.as_view(url="ingosapp/", permanent=True))
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    # path("duomenys/", include("ingosapp.urls"))

