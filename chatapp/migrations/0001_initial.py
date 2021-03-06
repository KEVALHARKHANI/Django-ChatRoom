# Generated by Django 3.0.6 on 2020-07-19 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activeuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('connected', models.BooleanField(default=False)),
                ('room', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chat_room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('message', models.CharField(max_length=800)),
                ('image', models.ImageField(upload_to='room_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Chat_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=900)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('room', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
