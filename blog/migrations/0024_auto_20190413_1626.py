# Generated by Django 2.0.13 on 2019-04-13 07:26

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20190413_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=blog.models.get_or_create_curry_category, on_delete=django.db.models.deletion.PROTECT, to='blog.Category', verbose_name='カテゴリ'),
        ),
    ]