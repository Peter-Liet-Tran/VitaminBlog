# Generated by Django 2.2.12 on 2020-08-12 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(default='', max_length=100),
        ),
    ]
