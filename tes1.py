import sqlite3 as sql

def print_all_passwords():
    try:
        con = sql.connect('C:/kuliah/semester 3/Pemrograman berbasis objek IoT/project_smart_home/smarthome.db')
        cur = con.cursor()
        cur.execute('SELECT password FROM user')
        passwords = cur.fetchall()
        for password in passwords:
            print(password[0])
        con.close()
    except Exception as e:
        print("Error:", e)

print_all_passwords()
