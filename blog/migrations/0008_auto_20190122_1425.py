# Generated by Django 2.1.5 on 2019-01-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured',
            field=models.ImageField(blank=True, default='featured/default.png', upload_to=''),
        ),
    ]