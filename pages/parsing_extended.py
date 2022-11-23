import logging
import time
import uuid
from typing import Optional

import psycopg2
import requests

from bs4 import BeautifulSoup


logging.getLogger(__name__)


def parse(url: str, connection) -> None:
    soup = get_raw(url)
    if soup:
        insert_page_data(
            connection=connection,
            id_=str(uuid.uuid4()),
            url=url,
        )
        for image_id, image_url in get_images(soup):
            insert_image_data(
                connection=connection,
                id_=image_id,
                url=image_url,
            )


def get_raw(url: str) -> Optional[BeautifulSoup]:
    try:
        raw_response = requests.get(url, timeout=3)
        time.sleep(2)
    except Exception:
        logging.error(f'URL {url} not connected!')
        return None
    logging.info(f'Url {url} parsed successfully!')
    return BeautifulSoup(raw_response.text, 'html.parser')


def get_images(soup: BeautifulSoup) -> list[tuple[str, str]]:
    images_data = [
        (str(uuid.uuid4()), image.get('src'))
        for image in soup.find_all('img')
    ]
    return images_data


def insert_page_data(connection, id_: str, url: str, valid: bool = True) -> None:
    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO urls (id, url, valid) VALUES (%s, %s, %s);',
            (id_, url, valid),
        )


def insert_image_data(connection, id_: str, url: str) -> None:
    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO images (id, url) VALUES (%s, %s);',
            (id_, url),
        )


def get_source_urls_from_csv(csv_file: str) -> list[str]:
    with open(csv_file) as file:
        return [i.split(',')[0] for i in file.readlines()][1:11]


def get_config() -> dict:
    return {
        'db_user': 'user',
        'db_pass': 'password',
        'db_name': 'user',
        'db_host': '127.0.0.1',
        'db_port': '5411',
        'csv_file_path': 'tests/ru.csv',
    }


def get_connection(config: dict):
    connection = psycopg2.connect(
        host=config['db_host'],
        user=config['db_user'],
        password=config['db_pass'],
        database=config['db_name'],
        port=config['db_port'],
    )
    connection.autocommit = True
    return connection


def parse_all():
    config = get_config()
    connection = get_connection(config)
    urls = get_source_urls_from_csv(config['csv_file_path'])
    if not urls:
        logging.error('File was not read!')
    for url in urls:
        parse(url, connection)


if __name__ == '__main__':
    parse_all()
