# Generated by Django 3.0.8 on 2020-08-05 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.CharField(max_length=40),
        ),
    ]