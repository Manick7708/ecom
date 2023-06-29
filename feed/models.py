from django.db import models
from django.contrib.auth.models import User
import datetime
import os
from import_export import resources

#

class PostFeed(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    description=models.CharField(max_length=255,blank=True,null=True)

class Image(models.Model):
    post=models.ForeignKey(PostFeed,on_delete=models.CASCADE,blank=True,null=True,related_name='post_image')
    image=models.ImageField()

class Like(models.Model):
    post=models.ForeignKey(PostFeed,on_delete=models.CASCADE,blank=True,null=True,related_name='image_like')
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='image_like')
    
class Comment(models.Model):
    post=models.ForeignKey(PostFeed,on_delete=models.CASCADE,blank=True,null=True,related_name='post_comment')  
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='post_comment')
    comment=models.CharField(max_length=255,blank=True,null=True)

class PostCommentLike(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='comment_like')
    post=models.ForeignKey(PostFeed,on_delete=models.CASCADE,blank=True,null=True,related_name='comment_like')

class ReplayComment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='post_replay_comment')
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,blank=True,null=True,related_name='post_replay_comment')
    replay_comment=models.CharField(max_length=244,blank=True,null=True)

class ReplayCommentLike(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='post_replay_like')
    replay_like=models.ForeignKey(ReplayComment,on_delete=models.CASCADE,blank=True,null=True,related_name='post_replay_like')    

class Share(models.Model):
    post=models.ForeignKey(Image,on_delete=models.CASCADE,blank=True,null=True,related_name='share_image')
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='share_image')
        
    
class Email(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    password=models.CharField(max_length=255,blank=True,null=True)
    email=models.CharField(max_length=255,blank=True,null=True)
    
class Car(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    model=models.CharField(max_length=255,blank=True,null=True)
    color=models.CharField(max_length=255,blank=True,null=True)
    cm=models.CharField(max_length=255,blank=True,null=True)
    
def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%M%D%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Catagory(models.Model):
    name=models.CharField(max_length=255,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=255,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-sho,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-trending")                                                                                                                                                                                                                                                                                                                                                                                                         
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
        
class Product(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name=models.CharField(max_length=255,null=False,blank=False)
    vendor=models.CharField(max_length=255,null=False,blank=False)
    product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    quantity=models.IntegerField(blank=False,null=False)
    original_price=models.FloatField(blank=False,null=False)
    selling_price=models.FloatField(blank=False,null=False)
    description=models.TextField(max_length=255,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-sho,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-trending")
    created_at=models.DateTimeField(auto_now_add=True)
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    Product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)