# Generated by Django 4.2.1 on 2023-06-01 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0005_alter_title_humans_alter_title_places'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
