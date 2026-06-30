import sqlite3

#A4
connect = sqlite3.connect("user.db")
#Рука и карандаш
cursor = connect.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name VARCHAR (30) NOT NULL, 
                   age INTEGER NOT NULL,
                   hobby TEXT
               )
''')

connect.commit()



# CRUD - Create - Read _ Update - Delete
                 
def create_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?,?,?)',
        (name, age, hobby)
    ) 
    connect.commit()
    print("Пользователь создан")
    
# create_user("Maxim", 27, "Горы-Лыжи-Спать")
# create_user("Ardager", 27, "Горы-Лыжи-Спать")
# create_user("Amir", 27, "Горы-Лыжи-Спать")
# create_user("Samira", 27, "Горы-Лыжи-Спать")



def get_users():
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    print(data)
    
#get_users()


def update_user(name, id):
    cursor.execute(
        'UPDATE users SET name = ? WHERE id = ?',
         (name, id)          
                   )
    connect.commit()
    print("Пользователь обновлен")
    
#update_user("Вася", 2)


def delete_user(id):
    cursor.execute(
        'DELETE FROM users WHERE id = ?',
        (id,)
    )
    connect.commit()
    print("Пользователь удален")
    

delete_user(5)
    