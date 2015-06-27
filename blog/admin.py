from django.contrib import admin
from blog.models import Category, Article

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article)