from django.contrib import admin

# Register your models here.
from .models import Author,Book,Publisher,Issue,UserProfile

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Issue)
admin.site.register(UserProfile)
