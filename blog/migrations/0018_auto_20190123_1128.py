# Generated by Django 2.1.5 on 2019-01-23 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190123_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='featuredimage',
            new_name='featured_image',
        ),
    ]