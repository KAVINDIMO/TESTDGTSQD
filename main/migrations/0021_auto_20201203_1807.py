# Generated by Django 3.1.2 on 2020-12-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20201203_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='img',
            field=models.ImageField(default='static/images/logo.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='img',
            field=models.ImageField(default='static/images/logo.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(default='static/images/logo.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(default='static/images/logo.png', upload_to='images'),
        ),
    ]