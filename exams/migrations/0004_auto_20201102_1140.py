# Generated by Django 3.1.2 on 2020-11-02 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams', '0003_auto_20201028_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_pin', models.CharField(max_length=8, unique=True, verbose_name='exam pin')),
                ('started_at', models.DateTimeField(verbose_name='valid from')),
                ('ended_at', models.DateTimeField(verbose_name='valid from')),
            ],
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='exam_question',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='desc_pre',
        ),
        migrations.RemoveField(
            model_name='question',
            name='uuid',
        ),
        migrations.AddField(
            model_name='examseries',
            name='duration',
            field=models.IntegerField(default=0, verbose_name='duration (minutes)'),
        ),
        migrations.AddField(
            model_name='question',
            name='rank',
            field=models.IntegerField(default=1, unique=True, verbose_name='rank'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_marked', models.BooleanField(default=False, verbose_name='marked for review')),
                ('is_answered', models.BooleanField(default=False, verbose_name='answer marked')),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_questions', to='exams.answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_questions', to='exams.question')),
                ('user_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_questions', to='exams.userexam')),
            ],
        ),
        migrations.AddField(
            model_name='userexam',
            name='exam_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_exams', to='exams.examseries'),
        ),
        migrations.AddField(
            model_name='userexam',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_exams', to=settings.AUTH_USER_MODEL),
        ),
    ]
