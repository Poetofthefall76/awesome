# Generated by Django 4.0.3 on 2022-03-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_image_title_alter_image_file_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
