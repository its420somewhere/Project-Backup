# Generated by Django 2.0.3 on 2018-04-07 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessUser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
