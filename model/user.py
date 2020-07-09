from peewee import Model, AutoField, IntegerField, CharField,\
    DateTimeField, BooleanField, TextField
from base.database.connection import db
import datetime

__all__ = ['AuthUser']


class AuthUser(Model):
    class Meta:
        database = db
        table_name = 'auth_user'

    id = AutoField()  # 用户id
    username = CharField(null=True)  # 用户编码
    password = CharField(null=True)  # 密码
