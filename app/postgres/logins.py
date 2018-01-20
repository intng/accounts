import os, psycopg2

import urllib.parse

result = urllib.parse.urlparse(os.getenv("postgres_uri"))
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname


def check_token(token):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            select = "SELECT * FROM tokens WHERE token = %s"
            cur.execute(select, (token,))
            res = cur.fetchall()
            if res:
                return res[0]
            else:
                return False


def create_token(id, token):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            insert = "INSERT INTO tokens (id, token) VALUES (%s, %s)"
            cur.execute(insert, (id, token))
            conn.commit()
            return True


def check_token_by_id(id):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            select = "SELECT * FROM tokens WHERE id = %s"
            cur.execute(select, (id,))
            res = cur.fetchall()
            if res:
                return res[0]
            else:
                return False


def delete_auth_token(token):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            delete = "DELETE FROM logins WHERE token = %s"
            cur.execute(delete, (token,))
            conn.commit()
            return True


def create_auth_token(id, token):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            insert = "INSERT INTO logins (id, token) VALUES (%s, %s)"
            cur.execute(insert, (id, token))
            conn.commit()
            return True


def check_auth_token(token):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            select = "SELECT * FROM logins WHERE token = %s"
            cur.execute(select, (str(token),))
            res = cur.fetchall()
            if res:
                return res[0]
            else:
                return False


def check_auth_token_by_id(id):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            select = "SELECT * FROM logins WHERE id = %s"
            cur.execute(select, (id,))
            res = cur.fetchall()
            if res:
                return res[0]
            else:
                return False
