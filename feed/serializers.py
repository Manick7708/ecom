from rest_framework import serializers
from.models import *


# class UserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model =User
#         fields=['name','password','phone','email']


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model =Image
        fields=['post','image']

class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model =Like
        fields=['post','user']

class ReplayCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model =ReplayComment
        fields=['user','comment','replay_comment'] 

class ReplayCommentLikeSerializers(serializers.ModelSerializer): 
    class Meta:
        model =ReplayCommentLike
        fields=['user','replay_like']
        
class PostCommentLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model =PostCommentLike
        fields=['post','user']


class ShareSerializers(serializers.ModelSerializer):
    class Meta:
        model =Share
        fields=['post','user']
        
class CommentSerializers(serializers.ModelSerializer):
    post_replay_comment=ReplayCommentSerializers(many=True)
    #post_replay_like=ReplayCommentLikeSerializers(many=True)
    # post_image=ImageSerializers(many=True)
    #replay_comment=ReplayCommentSerializers(many=True)
    #replay_like=ReplayCommentLikeSerializers(many=True)

    class Meta:
        model =Comment
        fields=['user','post','comment','post_replay_comment']


class PostFeedSerializers(serializers.ModelSerializer):
    post_image=ImageSerializers(many=True)
    image_like=LikeSerializers(many=True)
    post_comment=CommentSerializers(many=True)
    comment_like=PostCommentLikeSerializers(many=True)
    #replay_like=ReplayCommentLikeSerializers(many=True)
    #share_image=ShareSerializers(many=True)
    
    
    class Meta:
        model =PostFeed
        fields=['user','description','post_image','image_like','post_comment','comment_like']#'post_image']#,'image_like','post_comment','comment_like']