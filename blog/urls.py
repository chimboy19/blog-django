from django.urls import path
from . import views


urlpatterns=[
    path('register_user/',views.register_user,name='register_user'),
    path('create_blog/',views.create_blog,name='create_blog'),
    path('blog_list/',views.blog_list,name='blog_list'),
    path('blog_detail/<slug:slug>',views.blog_details,name='blog_detail'),
    path('update_blog/<int:pk>/',views.update_blog,name='update_blog'),
    path('delete_blog/<int:pk>/',views.delete_blog,name='delete_blog'),
    path('update_profile/',views.update_user_profile,name='update_user_profile')
   
]