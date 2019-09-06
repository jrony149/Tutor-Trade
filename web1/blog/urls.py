from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import(
    PostCreateView
    )

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('login/', views.login, name='blog-login'),  #the href links in the html pages are using the "names" here to link themselves with these url patterns which are of course calling functions from the Views.py file
    path('knowledge/', views.knowledge, name='blog-knowledge'),
    #path('postsign/',views.postsign, name='blog-knowledge'), #CC: added postsign path so when user signs up will redirect you to knowledge board
    path('signup/',views.signup, name='blog-signup'),
    path('postsignup/',views.postsignup, name='blog-postsignup'),
    path('contact/',views.contact, name='blog-contact'),
    path('postsign/', views.postsign),
    path('editProfile/',views.editProfile, name='blog-editProfile'),
    path('myProfile/', views.myProfile, name='blog-myProfile'),
    path('postprofile/', views.postprofile, name='blog-postprofile'),
    path('post/', PostCreateView.as_view(), name='blog-post_form'),
    path('passwordReset/', views.passwordReset, name='blog-passwordReset'),
    path('postpasswordreset/', views.postpasswordreset),
    path('createPost/', views.createpost, name='blog-createpost'),
    path('viewprofile/', views.viewprofile, name='blog-viewprofile'),
    path('postknowledge/', views.postknowledge, name='blog-postknowledge'),
    path('postcreatepost/', views.postcreatepost, name='blog-postcreatepost'),
    path('logout/', views.logout, name="blog-logout")
]



# CC note: you will not be able to access the knowledge board page unless you login. You may add
#      yourself manually from Verve-Slug-Tutor firebase console under the authentication tab to gain entrance!
