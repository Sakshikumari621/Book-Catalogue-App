# Generated by Django 5.0.1 on 2024-02-02 13:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("access", "0003_book_author_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="created_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
