# Generated by Django 3.0.6 on 2020-05-15 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.TextField(max_length=400),
        ),
    ]