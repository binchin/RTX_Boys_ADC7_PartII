# Generated by Django 3.0.2 on 2020-01-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
