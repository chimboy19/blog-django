from django.contrib import admin
from  django.contrib.auth.admin import UserAdmin
from .models import CustomUser ,Blog
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display=('username','email','first_name','last_name','profile_picture','linked_in','instagram','twitter')


class BlogAdmin(admin.ModelAdmin):
    list_display=('id','title','slug','content','category','featured_image','created_at','updated_at','published_date','is_draft')


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Blog,BlogAdmin)