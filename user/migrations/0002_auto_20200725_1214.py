# Generated by Django 3.0.6 on 2020-07-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='img2',
            field=models.ImageField(null=True, upload_to='portfolio'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='img3',
            field=models.ImageField(null=True, upload_to='portfolio'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='img4',
            field=models.ImageField(null=True, upload_to='portfolio'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='img5',
            field=models.ImageField(null=True, upload_to='portfolio'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='img6',
            field=models.ImageField(null=True, upload_to='portfolio'),
        ),
    ]
