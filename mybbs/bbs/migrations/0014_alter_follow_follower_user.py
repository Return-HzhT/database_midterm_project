# Generated by Django 4.2.1 on 2023-05-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bbs", "0013_comment_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="follow",
            name="follower_user",
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
