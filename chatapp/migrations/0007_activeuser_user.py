# Generated by Django 3.0.6 on 2020-07-19 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('chatapp', '0006_auto_20200719_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='activeuser',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.Student'),
            preserve_default=False,
        ),
    ]