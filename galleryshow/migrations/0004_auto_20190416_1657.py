# Generated by Django 2.2 on 2019-04-16 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleryshow', '0003_auto_20190415_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='default.gif', upload_to='images/'),
        ),
    ]