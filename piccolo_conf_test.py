from piccolo_conf import *  # noqa


DB = PostgresEngine(
    config={
        "database": "piccolo_project_test",
        "user": "murtazo",
        "password": "murtazo#1280",
        "host": "localhost",
        "port": 5432,
    }
)
