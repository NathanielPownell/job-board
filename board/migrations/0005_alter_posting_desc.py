# Generated by Django 4.0.4 on 2022-05-03 10:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_employer_avatar_alter_employer_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='desc',
            field=ckeditor.fields.RichTextField(max_length=2048),
        ),
    ]
