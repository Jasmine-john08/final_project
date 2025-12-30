from django.contrib import admin
from base.models import category,Article 

# Register your models here.
# admin.site.register(category)


class categoryAdmin(admin.ModelAdmin):
    list_display=['category_name']

admin.site.register(category,categoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','author','category','status','is_trending']
    prepopulated_fields={
        'slug':['title']
    }

admin.site.register(Article,ArticleAdmin)