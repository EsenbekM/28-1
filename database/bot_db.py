# SQL - Structured Query Language
import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute(
        "CREATE TABLE IF NOT EXISTS anketa "
        "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "telegram_id INTEGER UNIQUE, "
        "username VARCHAR (50), "
        "name VARCHAR (50), "
        "age INTEGER, "
        "gender VARCHAR (7), "
        "region TEXT, "
        "photo TEXT)"
    )

    db.execute(
        "CREATE TABLE IF NOT EXISTS users "
        "(telegram_id INTEGER PRIMARY KEY, "
        "username VARCHAR (50), "
        "full_name VARCHAR (50))"
    )

    db.commit()


async def sql_command_all_users():
    return cursor.execute("SELECT * FROM users").fetchall()


async def sql_command_insert_user(telegram_id, username, full_name):
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (telegram_id, username, full_name))
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa VALUES "
                       "(null, ?, ?, ?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random():
    users = cursor.execute("SELECT * FROM anketa").fetchall()
    random_user = random.choice(users)
    return random_user


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM anketa WHERE id == ?", (id,))
    db.commit()
