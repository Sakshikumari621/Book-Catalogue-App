# Generated by Django 5.0.1 on 2024-01-31 09:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("access", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="name",
            new_name="book_name",
        ),
        migrations.RemoveField(
            model_name="book",
            name="id",
        ),
        migrations.AddField(
            model_name="book",
            name="Book_id",
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
