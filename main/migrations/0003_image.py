# Generated by Django 4.0.3 on 2022-03-26 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_question_created_date_question_updated_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('file', models.FileField(upload_to='media')),
            ],
        ),
    ]
