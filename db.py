import sqlite3

def create_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE series (id INTEGER PRIMARY KEY, name TEXT, description TEXT)')
    cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')

    cursor.execute('INSERT INTO series (name, description) VALUES (?, ?)', ('BMW 3 Series', 'A compact executive car.'))
    cursor.execute('INSERT INTO series (name, description) VALUES (?, ?)', ('BMW 5 Series', 'A mid-sized executive car.'))
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', 'password'))

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_db()
