from django.shortcuts import redirect, render
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import * 
from .serializers import *
from.views import *
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import CustomUserForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserForm
from django.urls import path
from django.contrib.auth import authenticate,login,logout



# @api_view(['GET','POST'])
# @csrf_exempt
# def CreateUser(request):
#     if request.method == 'GET':
#         user=User.objects.all()
#         serializer=UserSerializers(user,many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer=User.objects.create(
#             name=request.data.get('name'),
#             password=request.data.get('password'),
#             phone=request.data.get('phone'),
#             email=request.data.get('email')
#         )
#         print(serializer)
#         return Response("save the data")
    
@api_view(['GET','POST'])
@csrf_exempt
def CreatePost(request):
    if request.method == 'GET':
        user=PostFeed.objects.prefetch_related('post_image','image_like','post_comment','comment_like').all()
        #print(user.post_image)
        serializer=PostFeedSerializers(user,many=True)
        return Response(serializer.data)
        print(hello)
        
    if request.method == 'POST':
        serializer=PostFeed.objects.create(
            user_id=request.data.get('user_id'),
            description=request.data.get('description')
        
        )
        print(serializer)
        return Response("save the data")

@api_view(['GET','POST'])
@csrf_exempt
def getImage(request):
    if request.method == 'GET':
        user=Image.objects.all()
        serializer=ImageSerializers(user,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=Image.objects.create(
            post_id=request.data.get('post_id'),
            image=request.data.get('image')
        
        )
        print(serializer)
        return Response("save the data")
    
@api_view(['GET','POST'])
@csrf_exempt
def getLike(request):
    if request.method == 'GET':
        like=Like.objects.all()
        serializer=LikeSerializers(like,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=Like.objects.create(
            post_id=request.data.get('post_id'),
            user_id=request.data.get('user_id')
            
        
        )
        print(serializer)
        return Response("save the data")
    
@api_view(['GET','POST'])
@csrf_exempt
def getLike(request):
    if request.method == 'GET':
        like=Like.objects.all()
        serializer=LikeSerializers(like,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=Like.objects.create(
            post_id=request.data.get('post_id'),
            user_id=request.data.get('user_id')
            
        
        )
        print(serializer)
        return Response("save the data")

@api_view(['GET','POST'])
@csrf_exempt
def getComment(request):
    if request.method == 'GET':
        like=Comment.objects.all()
        serializer=CommentSerializers(like,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=Comment.objects.create(
            post_id=request.data.get('post_id'),
            user_id=request.data.get('user_id'),
            comment=request.data.get('comment')
        )
        print(serializer)
        return Response("save the data")

@api_view(['GET','POST'])
@csrf_exempt
def getPostCommentLike(request):
    if request.method == 'GET':
        like=PostCommentLike.objects.all()
        serializer=PostCommentLikeSerializers(like,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=PostCommentLike.objects.create(
            post_id=request.data.get('post_id'),
            user_id=request.data.get('user_id')

        )
        print(serializer)
        return Response("save the data")

@api_view(['GET','POST'])
@csrf_exempt
def getReplayComment(request):
    if request.method == 'GET':
        like=ReplayComment.objects.all()
        serializer=ReplayCommentSerializers(like,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=ReplayComment.objects.create(
            user_id=request.data.get('user_id'),
            comment_id=request.data.get('comment_id'),
            replay_comment=request.data.get('replay_comment')
        )
        print(serializer)
        return Response("save the data")

@api_view(['GET','POST'])
@csrf_exempt
def getShare(request):
    if request.method == 'GET':
        share=Share.objects.all()
        serializer=ShareSerializers(share,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=Share.objects.create(
            post_id=request.data.get('post_id'), 
            user_id=request.data.get('user_id')
        )
        print(serializer)
        return Response("save the data")
    
@api_view(['GET','POST'])
@csrf_exempt
def getReplayCommentLike(request):
    if request.method == 'GET':
        like=ReplayCommentLike.objects.all()
        serializer=ReplayCommentLikeSerializers(like,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=ReplayCommentLike.objects.create(
            user_id=request.data.get('user_id'),
            replay_like_id=request.data.get('replay_like_id')
        )
        print(serializer)
        return Response("save the data")
    
# def say_hello (request): 
#     return render(request,'index.html')

def hello (request): 
    products=Product.objects.filter(trending=1)
    return render(request,'manik.html',{"products": products})

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
    return redirect("/feed/register/login")

def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=name, password=pwd)
        if user is not None:  
            login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect("/feed/login/register")
        else:
            messages.error(request, "Invalid User Name or Password")
    return render(request, 'login.html')


def register(request):
    forms = CustomUserForm()
    if request.method == 'POST':
        forms = CustomUserForm(request.POST)
        print(forms)
        if forms.is_valid():
            #forms.save()
            print(forms)
            messages.success(request, "Registration Success! You can login now.")
            return redirect('/feed/login')
    return render(request, 'register.html', {"forms": forms})


def collections (request): 
    catagory=Catagory.objects.all()
    return render(request,'collections.html',{"catagory":catagory})




def collectionsview(request, name):
    category = Catagory.objects.get(name=name)
    if category.status == 1:
        products=Product.objects.filter(catagory__name=name)
        return render(request, 'layouts/products/index.html', {"products": products,"category_name":name})
    else:
        messages.warning(request, "No Such Category Found")
        return redirect('collections')

def my_view(request):
    contex = {
        'message':'hello,world'
    }
    return render(request,'feed/index.html',contex)

def members(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render)




def say_hell (request):
    #queryset = product.objects.filter(uit_price_range(20,30))
    return render(request,'vasu.html',{'name' :'Arul'})#'products':List (queryset))


def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=1)):
        if(Product.objects.filter(name=pname,status=1)):
            products=Product.objects.filter(name=pname,status=1).first()
            return render(request, 'layouts/products/product_details.html',{"products": products})
        else:
            messages.error(request,"No Such Product Found")
            return redirect('collections')
    else:
        messages.error(request,"No Such Catagory Found")
        return redirect('collections')
