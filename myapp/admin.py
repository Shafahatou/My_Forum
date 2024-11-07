from django.contrib import admin
from .models import Category, Article, Tag, Comment, AdditionalImage #,PopularPost

# Register your models here.


admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(AdditionalImage)

#admin.site.register(PopularPost)
