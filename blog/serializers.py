from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Blog



class updateUserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=['id','username','email','first_name','last_name','profile_picture','linked_in','instagram','twitter']


class UserRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=['id','username','first_name','last_name','password']
        extra_kwargs={
            'password':{'write_only':True}
        }



    def create(self, validated_data):
        User = get_user_model()
        user = User.objects.create(
            username=validated_data['username'],
            # email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user  
    

class SimpleAuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=['id','first_name','username','last_name','profile_picture']



class BlogSerializers(serializers.ModelSerializer):
    author = SimpleAuthorSerializers(read_only=True)
    # category = serializers.StringRelatedField()

    class Meta:
        model = Blog
        fields = [
            'id','title','slug','author','content',
            'category',
            'featured_image','created_at','updated_at',
            'published_date','is_draft'
        ]
