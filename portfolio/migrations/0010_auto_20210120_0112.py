# Generated by Django 3.1.5 on 2021-01-20 04:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20210118_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='trajectory',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='trajectory',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='trajectory',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Titulo'),
        ),
    ]
