# Generated by Django 4.0.4 on 2022-05-02 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_posting_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='uploads/avatars'),
        ),
    ]
