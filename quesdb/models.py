from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Squiz(models.Model):
    squizno = models.CharField(primary_key=True, max_length=11)
    scontent = models.CharField(max_length=200, blank=True, null=True)
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    setter = models.ForeignKey(User, models.DO_NOTHING, db_column='setter', blank=True, null=True)

    class Meta:
        db_table = 'squiz'


class Sanswer(models.Model):
    qno = models.ForeignKey('Squiz', models.DO_NOTHING, db_column='qno',primary_key=True)
    respondent = models.ForeignKey(User, models.DO_NOTHING,db_column='respondent')
    ssolution = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'sanswer'
        unique_together = (('qno', 'respondent'),)


class Tquiz(models.Model):
    setter = models.ForeignKey(User, models.DO_NOTHING, db_column='setter',blank=True, null=True)
    tquizno = models.CharField(primary_key=True, max_length=11)
    tquizcontent = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'tquiz'


class Tanswer(models.Model):
    qno = models.ForeignKey('Tquiz', models.DO_NOTHING, db_column='qno', primary_key=True)
    respondent = models.ForeignKey(User, models.DO_NOTHING, db_column='respondent')
    tsolution = models.CharField(max_length=200)

    class Meta:
        db_table = 'tanswer'
        unique_together = (('qno', 'respondent'),)


class Score(models.Model):
    num = models.AutoField(primary_key=True)
    setter = models.ForeignKey(User, models.DO_NOTHING, db_column='setter', blank=True,related_name="score_setter", null=True)
    respondent = models.ForeignKey(User, models.DO_NOTHING, db_column='respondent', blank=True, related_name="score_respondent",null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'score'
        unique_together=(('setter','respondent'),)














