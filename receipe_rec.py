import pymysql
import os

class ReceipeRec:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = "admin"
        pw = "dbuserdbuser"
        h = "userdb.ci9bmsfj6m9q.us-east-1.rds.amazonaws.com"

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_random_receipe():

        sql = "SELECT t.* FROM receipe_schema.RAW_recipes t ORDER BY RAND() LIMIT 20";
        conn = ReceipeRec._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchone()

        return result

