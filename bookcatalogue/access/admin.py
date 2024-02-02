from django.contrib import admin
from access.models import Book


class bookAdmin(admin.ModelAdmin):
    list_display = (
        "Book_id",
        "user",
        "book_name",
        "author_name",
        "year_of_release",
        "description",
        "rating",
        "comment",
        "public",
        "created_at",
    )


admin.site.register(Book, bookAdmin)
