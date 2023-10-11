from django.urls import path
from .views import *

urlpatterns = [
    path('analysis/', FiberView.as_view(), name="fiber"),
    path('magnesium/', MgView.as_view(), name='magnesium'),
    path('zinc/', ZnView.as_view(), name='zinc'),
    path('folicacid', FaView.as_view(), name='folicacid'),
    path('phosphor/', PView.as_view(), name='phosphor'),
    path('vitaminA/', VitAView.as_view(), name='vitaminA'),
    path('vitaminC/', VitCView.as_view(), name='vitaminC'),
    path('vitaminE/', VitEView.as_view(), name='vitaminE'),
    path('thebest/', TheBestView.as_view(), name='best'),
]
