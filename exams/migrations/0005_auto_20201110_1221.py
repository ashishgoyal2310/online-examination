# Generated by Django 3.1.2 on 2020-11-10 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_auto_20201102_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexam',
            name='ended_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ended At'),
        ),
        migrations.AlterField(
            model_name='userexam',
            name='started_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Started At'),
        ),
    ]
