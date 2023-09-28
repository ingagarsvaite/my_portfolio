from django.urls import path, include
from .views import PostList, PostDetail, CommentList, CommentDetail

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('comments/<int:pk>', CommentList.as_view()),
    path('comment/<int:pk>', CommentDetail.as_view()),
]