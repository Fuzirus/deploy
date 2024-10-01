from mysql.connector import connect
from backend.settings import database_config
from copy import deepcopy


class MysqlConnector:
    _table = "items"

    def __init__(self):
        self._connector = connect(**database_config)
        self._cursor = self._connector.cursor()

    @staticmethod
    def _create_database():
        to_create_conf = deepcopy(database_config)
        to_create_conf.pop("database")
        _connector = connect(**to_create_conf)
        _cursor = _connector.cursor()
        _cursor.execute("CREATE DATABASE IF NOT EXISTS notes;")

    def _create_table(self):
        self._cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self._table} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
        )

    def get_items(self):
        self._cursor.execute(f"SELECT * FROM {self._table} order by id asc;")
        return [('%s. %s' % row) for row in self._cursor.fetchall()]

    def insert_item(self, value):
        sql = f"INSERT INTO {self._table} (name) VALUES (%s)"
        self._cursor.execute(sql, (value, ))
        self._connector.commit()
