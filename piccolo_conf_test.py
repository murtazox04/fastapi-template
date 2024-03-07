from piccolo_conf import *  # noqa

from decouple import config


DB = PostgresEngine(
    config={
        "database": config("DB_NAME"),
        "user": config("DB_USER"),
        "password": config("DB_PASSWORD"),
        "host": config("DB_HOST"),
        "port": config("DB_PORT"),
    }
)
