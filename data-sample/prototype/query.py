import sqlite3
from sqlite3 import *

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_role_by_user_id(conn, user_id):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT admin_status FROM user WHERE user_id=?", (user_id,))

    rows = cur.fetchone()

    if rows is None:
        return 0
    return rows[0]