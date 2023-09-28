from rest_framework import serializers
from .models import Post, Comment, CommentLike, PostLike


# class CommentSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.username')
#     user_id = serializers.ReadOnlyField(source='user.id')
#
#     class Meta:
#         model = Comment
#         fields = ['id', 'user', 'user_id', 'post', 'body', 'created']
class PostSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer()
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'body', 'created']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = ['id', 'user', 'user_id', 'post', 'body', 'created']


# class PostDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#             model = Post
#             fields = ['id', 'user', 'title', 'body', 'created']

