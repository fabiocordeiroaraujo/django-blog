from django.contrib import admin
from blog.models import Post, Category, Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    pass

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass

admin.site.register(Image, ImageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
