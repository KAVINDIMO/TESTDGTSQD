# Generated by Django 3.1.2 on 2020-12-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20201204_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default='static/images/14358.jpg', upload_to='images'),
        ),
    ]
