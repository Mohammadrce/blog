from django.contrib import admin
from .models import Article, Category, Comment, ContactUs,Like

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ContactUs)
admin.site.register(Like)