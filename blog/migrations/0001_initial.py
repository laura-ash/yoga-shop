# Generated by Django 3.1.3 on 2021-01-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.CharField(blank=True, max_length=140, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]