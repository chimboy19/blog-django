from django.shortcuts import render,HttpResponse,get_object_or_404
from rest_framework.response import Response
from .serializers import UserRegistrationSerializers , BlogSerializers,updateUserProfileSerializers
from .models import Blog
from rest_framework import status
from rest_framework .pagination import PageNumberPagination
from rest_framework . permissions import IsAuthenticated,AllowAny
from rest_framework . decorators import api_view ,permission_classes 



class BlogListPagination(PageNumberPagination):
    page_size=3

@api_view(["POST"])
def register_user(request):
    serializer= UserRegistrationSerializers(data= request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user=request.user
    serializer=updateUserProfileSerializers(user,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_blog(request):
    user=request.user
    serializer=BlogSerializers(data= request.data)

    if serializer.is_valid():
        serializer.save(author=user)
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([AllowAny])
def blog_list(request):
    blogs= Blog.objects.all()
    paginator=BlogListPagination()
    paginator_blogs = paginator.paginate_queryset(blogs, request)
    Serializers=BlogSerializers(paginator_blogs,many=True)
    return paginator.get_paginated_response(Serializers.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def blog_details(request, slug):
    blog=get_object_or_404(Blog,slug=slug)
    serializer=BlogSerializers(blog)
    return Response(serializer.data)





@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_blog(request,pk):
    user=request.user
    blog=Blog.objects.get(id=pk)
    if blog.author !=user:
        return Response ({"error": "you are not the author of this blog"}, status=status.HTTP_403_FORBIDDEN)
    serializer=BlogSerializers(blog,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def delete_blog(request,pk):
    user=request.user
    blog=Blog.objects.get(id=pk)
    if blog.author !=user:
        return Response ({"error": "you are not the author of this blog"}, status=status.HTTP_403_FORBIDDEN)
    blog.delete()
    return Response({"message": "blog has been delete successfully "}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def get_blog_categories(request):
    categories = [choice[0] for choice in Blog.CATEGORY]
    return Response(categories)