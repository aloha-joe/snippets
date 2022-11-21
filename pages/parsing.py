import requests
import psycopg2
import uuid
import time
from bs4 import BeautifulSoup
from config import host, user, password, db_name, port

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name,
    port=port
)
connection.autocommit = True

with connection.cursor() as cursor:
    cursor.execute(
        """CREATE TABLE urls (id varchar, url varchar, valid bool DEFAULT true); \n 
        CREATE TABLE images (id varchar, url varchar);"""
    )

target_list = []
def image_parsing(target):
    r = requests.get(target)
    soup = BeautifulSoup(r.text, 'html.parser')
    if soup:
        with connection.cursor() as cursor:
            cursor.execute("""
            INSERT INTO urls (id, url, valid)
            VALUES (%s, %s, %s);""",
                           (str(uuid.uuid4()), target, True)
                           )
        link_list = []
    for link in soup.find_all('img'):
        with connection.cursor() as cursor:
            if str(link.get('src')) not in link_list:
                cursor.execute("""
                INSERT INTO images (id, url)
                VALUES (%s, %s);""",
                               (str(uuid.uuid4()), str(link.get('src')))
                               )
                link_list.append(str(link.get('src')))
    return link_list


with open('/home/aloha/Projects/snippets/tests/ru.csv') as inf:
    for target_link in inf:
        target_link = inf.readline().strip().rsplit(',', 15)
        target_list.append(target_link[0])

for link in target_list:
    image_parsing(link)
    time.sleep(5)

if connection:
    connection.close()
    print('connection closed')
