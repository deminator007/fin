import psycopg2 as pg
from config import user, host, password, db_name
with pg.connect(
		user=user,
		host=host,
        password=password,
		database=db_name
) as cn:
    cn.autocommit = True
def create_database():
    with cn.cursor() as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS companion(id serial, id_vk varchar(50) PRIMARY KEY);"
        )
def delete_database():
    with cn.cursor() as cursor:
        cursor.execute(
            "DROP TABLE  IF EXISTS companion CASCADE;"
        )
def insert_info(id_vk):
    with cn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO companion(id_vk) VALUES(%s)",
            (id_vk,)
        )
create_database()