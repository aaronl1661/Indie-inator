# Generated by Django 3.0.8 on 2020-07-24 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200722_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[], max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='playlist',
            name='playlist',
            field=models.CharField(max_length=30),
        ),
    ]
