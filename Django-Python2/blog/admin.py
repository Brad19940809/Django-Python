from django.contrib import admin
from blog.models import Blog, Catagory, Tag

# Register your models here.
admin.site.register(Blog)
admin.site.register(Catagory)
admin.site.register(Tag)
# admin.site.register([Catagory,Tag,Blog])
