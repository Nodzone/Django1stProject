# Generated by Django 3.1.6 on 2021-02-07 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20210206_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_img',
            field=models.ImageField(blank=True, null=True, upload_to='cover/'),
        ),
    ]