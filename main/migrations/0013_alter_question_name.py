# Generated by Django 4.0.3 on 2022-04-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_question_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
