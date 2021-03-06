# Generated by Django 2.2.7 on 2020-02-07 03:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productmanagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderID', models.IntegerField()),
                ('accessories', models.ManyToManyField(blank=True, to='productmanagement.Accessories')),
                ('customer', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('phone', models.ManyToManyField(blank=True, to='productmanagement.Phones')),
            ],
        ),
    ]
