# Generated by Django 3.2.8 on 2021-11-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_auto_20211108_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='is_user_uploaded',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='exam',
            name='source',
            field=models.CharField(max_length=200),
        ),
    ]