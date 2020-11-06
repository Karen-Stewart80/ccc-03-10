import psycopg2
from dotenv import load_dotenv

import os
load_dotenv()

connection = psycopg2.connect(
    database="library_api",
    user="app",
    password=os.getenv("db_password"),
    host="localhost"
)

cursor = connection.cursor()

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()
