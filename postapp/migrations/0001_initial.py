# Generated by Django 5.0 on 2023-12-10 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('short_desc', models.CharField(max_length=250)),
                ('body', models.TextField()),
            ],
        ),
    ]
