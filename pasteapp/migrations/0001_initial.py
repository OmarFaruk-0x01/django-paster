# Generated by Django 2.2.1 on 2019-05-23 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Syntax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('extension', models.CharField(blank=True, max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('popular', models.BooleanField(default=True)),
            ],
        ),
    ]
