# Generated by Django 3.0.8 on 2020-12-05 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects', verbose_name='Imagen'),
        ),
    ]