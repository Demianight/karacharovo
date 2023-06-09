# Generated by Django 4.2.1 on 2023-06-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0004_alter_title_humans_alter_title_places'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='humans',
            field=models.ManyToManyField(blank=True, related_name='titles', to='titles.human'),
        ),
        migrations.AlterField(
            model_name='title',
            name='places',
            field=models.ManyToManyField(blank=True, related_name='titles', to='titles.place'),
        ),
    ]
