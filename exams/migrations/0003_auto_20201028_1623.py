# Generated by Django 2.0 on 2020-10-28 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20201028_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='desc_pre',
            field=models.TextField(blank=True, default='', verbose_name='description preformatted'),
        ),
    ]
