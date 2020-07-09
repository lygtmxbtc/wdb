from peewee import PostgresqlDatabase, ExceptionWrapper, EXCEPTIONS, SENTINEL
import psycopg2.extras
from ..cfg_parser import BaseConfig

__exception_wrapper__ = ExceptionWrapper(EXCEPTIONS)


class HermesDatabase(PostgresqlDatabase):
    def __init__(self, *args, **kwargs):
        super(HermesDatabase, self).__init__(*args, **kwargs)

    def dict_cursor(self, commit=None):
        if self.is_closed():
            self.connect()
        return self._state.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def dict_execute_sql(self, sql, params=None, commit=SENTINEL):
        if commit is SENTINEL:
            if self.in_transaction():
                commit = False
            elif self.commit_select:
                commit = True
            else:
                commit = not sql[:6].lower().startswith('select')

        with __exception_wrapper__:
            cursor = self.dict_cursor(commit)
            try:
                cursor.execute(sql, params or ())
            except Exception:
                if self.autorollback and not self.in_transaction():
                    self.rollback()
                raise
            else:
                if commit and not self.in_transaction():
                    self.commit()
        return cursor


db = HermesDatabase(
    database=BaseConfig.db_name,
    user=BaseConfig.db_username,
    password=BaseConfig.db_password,
    host=BaseConfig.db_addr,
    port=BaseConfig.db_port,
)
