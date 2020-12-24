# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_post'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Login(models.Model):
    lid = models.ForeignKey('Users', models.DO_NOTHING, db_column='lid', primary_key=True)
    lpassword = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


class Noteboard(models.Model):
    nhost = models.ForeignKey('Users', models.DO_NOTHING, db_column='nhost', primary_key=True)
    nguest = models.ForeignKey('Users', models.DO_NOTHING, db_column='nguest')
    npraise = models.IntegerField(blank=True, null=True)
    nunnamed = models.CharField(max_length=3, blank=True, null=True)
    ncontent = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noteboard'
        unique_together = (('nhost', 'nguest'),)


class Otherstick(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', primary_key=True)
    tid = models.ForeignKey('Tag', models.DO_NOTHING, db_column='tid')

    class Meta:
        managed = False
        db_table = 'otherstick'
        unique_together = (('uid', 'tid'),)


class Questiondb(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', primary_key=True)
    qno = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'questiondb'
        unique_together = (('uid', 'qno'),)


class Sanswer(models.Model):
    qno = models.ForeignKey(Questiondb, models.DO_NOTHING, db_column='qno', primary_key=True)
    setter = models.ForeignKey(Questiondb, models.DO_NOTHING, db_column='setter')
    respondent = models.ForeignKey('Users', models.DO_NOTHING, db_column='respondent')
    ssolution = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sanswer'
        unique_together = (('qno', 'setter', 'respondent'),)


class Secretlove(models.Model):
    sllow = models.ForeignKey('Users', models.DO_NOTHING, db_column='sllow', primary_key=True)
    slhigh = models.ForeignKey('Users', models.DO_NOTHING, db_column='slhigh')

    class Meta:
        managed = False
        db_table = 'secretlove'
        unique_together = (('sllow', 'slhigh'),)


class Selfstick(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', primary_key=True)
    tid = models.ForeignKey('Tag', models.DO_NOTHING, db_column='tid')

    class Meta:
        managed = False
        db_table = 'selfstick'
        unique_together = (('uid', 'tid'),)


class Squiz(models.Model):
    squizno = models.ForeignKey(Questiondb, models.DO_NOTHING, db_column='squizno')
    scontent = models.CharField(max_length=200, blank=True, null=True)
    a = models.CharField(db_column='A', max_length=100, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c = models.CharField(db_column='C', max_length=100, blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(db_column='D', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e = models.CharField(db_column='E', max_length=100, blank=True, null=True)  # Field name made lowercase.
    setter = models.ForeignKey(Questiondb, models.DO_NOTHING, db_column='setter', primary_key=True)

    class Meta:
        managed = False
        db_table = 'squiz'
        unique_together = (('setter', 'squizno'),)


class Tag(models.Model):
    tid = models.IntegerField(primary_key=True)
    tlike = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag'


class Tanswer(models.Model):
    qno = models.ForeignKey(Questiondb, models.DO_NOTHING, db_column='qno', primary_key=True)
    setter = models.ForeignKey(Questiondb, models.DO_NOTHING, db_column='setter')
    respondent = models.ForeignKey('Users', models.DO_NOTHING, db_column='respondent')
    tsolution = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tanswer'
        unique_together = (('qno', 'setter', 'respondent'),)


class Tquiz(models.Model):
    setter = models.ForeignKey(Questiondb, models.DO_NOTHING, db_column='setter', primary_key=True)
    tquizno = models.ForeignKey(Questiondb, models.DO_NOTHING, db_column='tquizno')
    tquizcontent = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tquiz'
        unique_together = (('setter', 'tquizno'),)


class Users(models.Model):
    uid = models.IntegerField(primary_key=True)
    uname = models.CharField(unique=True, max_length=20, blank=True, null=True)
    ugender = models.CharField(max_length=1, blank=True, null=True)
    usexlike = models.CharField(max_length=2, blank=True, null=True)
    uage = models.SmallIntegerField(blank=True, null=True)
    uprovince = models.CharField(max_length=20, blank=True, null=True)
    uschool = models.CharField(max_length=40, blank=True, null=True)
    umajor = models.CharField(max_length=20, blank=True, null=True)
    ubirthday = models.DateField(blank=True, null=True)
    ustate = models.CharField(max_length=2, blank=True, null=True)
    umail = models.CharField(unique=True, max_length=20, blank=True, null=True)
    usentence = models.CharField(max_length=100, blank=True, null=True)
    upraise = models.IntegerField(blank=True, null=True)
    upicture = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersProfile(models.Model):
    image = models.CharField(max_length=100)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'users_profile'
