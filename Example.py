import sqlite3


# создание БД
conn = sqlite3.connect('delivery.db', check_same_thread=False)
# thon + SQL
sql = conn.cursor()


# создание таблицы пользователей
sql.execute('CREATE TABLE IF NOT EXISTS users '
            '(id INTEGER, name TEXT, number TEXT, location, TEXT);')
# создание таблицы продуктов
sql.execute('CREATE TABLE IF NOT EXISTS products '
            '(pr_id INTEGER AUTOINCREMENT, '
            'pr_name TEXT, pr_des TEXT, pr_price REAL, '
            'pr_photo TEXT, pr_count INTEGER);')
# Создание таблицы
sql.execute('CREATE TABLE IF NOT EXISTS cart '
            '(user_id INTEGER, user_product TEXT, '
            'user_quantity INTEGER);')


