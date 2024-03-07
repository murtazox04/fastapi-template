from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

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

APP_REGISTRY = AppRegistry(
    apps=["home.piccolo_app", "piccolo_admin.piccolo_app"]
)
