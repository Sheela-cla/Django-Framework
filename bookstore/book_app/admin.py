from django.contrib import admin
from book_app.models import Category,BookInfo
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list= ['name']

class BookInfoAdmin(admin.ModelAdmin):
    list = ['title','author','description','price','categories','publication_date','cover_image']
    list_filter = ['categories', 'author']
    search_fields = ['title', 'author']

admin.site.register(Category,CategoryAdmin)
admin.site.register(BookInfo,BookInfoAdmin)