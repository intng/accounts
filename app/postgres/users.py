import os, psycopg2

import urllib.parse

result = urllib.parse.urlparse(os.getenv("postgres_uri"))
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname


def find_by_vk_id(vk_id):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            select = "SELECT * FROM users WHERE vk_id = %s"
            cur.execute(select, (vk_id,))
            res = cur.fetchall()
            if res:
                return res[0]
            else:
                return False


def find_by_tg_id(tg_id):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            select = "SELECT * FROM users WHERE tg_id = %s"
            cur.execute(select, (tg_id,))
            res = cur.fetchall()
            if res:
                return res[0]
            else:
                return False


def find_by_schoolcard(schoolcard):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            select = "SELECT * FROM users WHERE schoolcard = %s"
            cur.execute(select, (schoolcard,))
            res = cur.fetchall()
            if res:
                return res[0]
            else:
                return False


def create(id, name, surname, schoolcard, approved, form, vk_id, tg_id):
    with psycopg2.connect(database=database, user=username, password=password, host=hostname) as conn:
        with conn.cursor() as cur:
            insert = "INSERT INTO users (id, name, surname, schoolcard, approved, form, vk_id, tg_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(insert, (id, name, surname, schoolcard, approved, form, vk_id, tg_id))
            conn.commit()
            return True
