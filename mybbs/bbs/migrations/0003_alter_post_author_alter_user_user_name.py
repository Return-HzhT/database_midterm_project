# Generated by Django 4.2.1 on 2023-05-24 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bbs", "0002_rename_article_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="bbs.user"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_name",
            field=models.CharField(max_length=32, unique=True),
        ),
    ]