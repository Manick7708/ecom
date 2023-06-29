import statistics
from django.conf import Settings, SettingsReference, settings
from django.contrib import admin
from django.urls import path,include
from .models import *
from .views import *
from feed import views
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
   # path('create_user/',CreateUser),
    #path('create_post/',CreatePost),
    path('create_image/',getImage),
    path('create_like/',getLike),
    path('create_comment/',getComment),
    path('create_comment_like/',getPostCommentLike),
    path('create_replay_comment/',getReplayComment),
    path('create_replay_like/',getReplayCommentLike),
    path('create_share/',getShare),
    #path('vasu/',views.say_hell),
    path('', views.hello, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('collection/', views.collections, name='collections'),
    path('collection/<str:name>/', views.collectionsview, name='collections'),
    #path('feed/collection/<str:name>/', views.collections, name='collections'),

    path('collection/<str:cname>/<str:pname>/', views.product_details, name='product_details'),
]


if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    



