# Generated by Django 4.2.1 on 2023-05-26 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bbs", "0012_remove_comment_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="body",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
