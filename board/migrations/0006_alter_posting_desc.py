# Generated by Django 4.0.4 on 2022-05-03 10:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_alter_posting_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='desc',
            field=ckeditor.fields.RichTextField(max_length=4048),
        ),
    ]
