from django.contrib import admin
# Import models here
from freeshelf.models import Book, Category

#Adds Category to Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

#Makes automatic slug creation
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title', 'author', 'description', 'date_added', 'image')
    prepopulated_fields = {'slug': ('title',)}

# Register models here
admin.site.register(Book, BookAdmin)
