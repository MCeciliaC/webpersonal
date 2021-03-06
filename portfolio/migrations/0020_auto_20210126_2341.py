# Generated by Django 3.1.5 on 2021-01-27 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_project_der'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Titulo')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Crédito',
            },
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-order'], 'verbose_name': 'proyecto', 'verbose_name_plural': 'proyectos'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
    ]
