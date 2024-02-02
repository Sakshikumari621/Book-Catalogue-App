from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    Book_id = models.AutoField(primary_key=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200, null=True)
    year_of_release = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, null=True)

    @property
    def rating_color(self):
        if self.rating <= 2:
            return "red"
        elif self.rating <= 3.5:
            return "yellow"
        else:
            return "green"

    def __str__(self):
        return self.book_name
