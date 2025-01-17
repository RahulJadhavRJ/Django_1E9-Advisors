# Generated by Django 4.2.13 on 2024-07-03 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0002_addvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='JsonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField(max_length=100)),
                ('lname', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.TextField(max_length=100)),
                ('location', models.TextField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
