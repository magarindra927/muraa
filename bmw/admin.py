from django.contrib import admin
from .models import Indra, Magar, Thapa, Category, Copyright

# Register your models here.
@admin.register(Indra)
class IndraAdmin(admin.ModelAdmin):
    list_display=['id','name','slug']
    prepopulated_fields={'slug':('name',)}

@admin.register(Magar)
class MagarAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'photo', 'indra']  
    prepopulated_fields={'slug':('title',)}  


@admin.register(Thapa)
class ThapaAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'photo']    


@admin.register(Category)
class CategroyAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'slug', 'photo']
    prepopulated_fields={'slug':('title',)}    


@admin.register(Copyright)
class CopyrightAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'slug', 'photo']
    prepopulated_fields={'slug':('title',)}    