# Generated by Django 2.2.1 on 2019-06-04 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Squiz',
            fields=[
                ('squizno', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('scontent', models.CharField(blank=True, max_length=200, null=True)),
                ('a', models.CharField(blank=True, db_column='A', max_length=100, null=True)),
                ('b', models.CharField(blank=True, db_column='B', max_length=100, null=True)),
                ('c', models.CharField(blank=True, db_column='C', max_length=100, null=True)),
                ('d', models.CharField(blank=True, db_column='D', max_length=100, null=True)),
                ('e', models.CharField(blank=True, db_column='E', max_length=100, null=True)),
                ('setter', models.ForeignKey(blank=True, db_column='setter', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'squiz',
            },
        ),
        migrations.CreateModel(
            name='Tquiz',
            fields=[
                ('tquizno', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('tquizcontent', models.CharField(blank=True, max_length=200, null=True)),
                ('setter', models.ForeignKey(blank=True, db_column='setter', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tquiz',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('respondent', models.ForeignKey(blank=True, db_column='respondent', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='score_respondent', to=settings.AUTH_USER_MODEL)),
                ('setter', models.ForeignKey(blank=True, db_column='setter', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='score_setter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'score',
                'unique_together': {('setter', 'respondent')},
            },
        ),
        migrations.CreateModel(
            name='Tanswer',
            fields=[
                ('qno', models.ForeignKey(db_column='qno', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='quesdb.Tquiz')),
                ('tsolution', models.CharField(max_length=200)),
                ('respondent', models.ForeignKey(db_column='respondent', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tanswer',
                'unique_together': {('qno', 'respondent')},
            },
        ),
        migrations.CreateModel(
            name='Sanswer',
            fields=[
                ('qno', models.ForeignKey(db_column='qno', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='quesdb.Squiz')),
                ('ssolution', models.CharField(blank=True, max_length=1, null=True)),
                ('respondent', models.ForeignKey(db_column='respondent', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sanswer',
                'unique_together': {('qno', 'respondent')},
            },
        ),
    ]
