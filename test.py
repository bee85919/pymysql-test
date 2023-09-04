import os
from dotenv import load_dotenv
import pymysql


load_dotenv()


DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT", 3306)  # .env 파일에서 없으면 3306으로 설정
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")


db_config = {
    "host": DB_HOST,
    "port": int(DB_PORT),
    "db": DB_NAME,
    "user": DB_USER,
    "password": DB_PASSWORD,
    "charset": "utf8"
}
print("DB Config:", db_config)


# pymysql을 이용해 DB 연결
db = pymysql.connect(**db_config)