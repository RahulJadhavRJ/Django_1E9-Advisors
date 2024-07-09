# Generated by Django 4.2.13 on 2024-06-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('descr', models.TextField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField()),
            ],
        ),
    ]