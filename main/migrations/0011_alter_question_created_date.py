# Generated by Django 4.0.3 on 2022-03-27 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_question_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
