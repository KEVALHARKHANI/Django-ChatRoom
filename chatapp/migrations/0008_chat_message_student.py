# Generated by Django 3.0.6 on 2020-07-20 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('chatapp', '0007_activeuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_message',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.Student'),
            preserve_default=False,
        ),
    ]
