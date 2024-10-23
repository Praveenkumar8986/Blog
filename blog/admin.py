from django.contrib import admin
from blog.models import post
# Register your models here.
class postadmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('status','author','created')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
admin.site.register(post,postadmin)