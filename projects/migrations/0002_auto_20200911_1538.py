# Generated by Django 3.0.6 on 2020-09-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.FilePathField(default='/img/project1.png', path='/img'),
        ),
    ]