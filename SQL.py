import sqlite3 as sql
'''
list fungsi:

#main table
home()
user_type()
user()
room()
electronics()
sensor()

#change
change_sensor(ID, data)
change_pass(username, new_pass)
change_electronics_room(val, user, time) - > ada 11 fungsi, untuk ganti on ke off sebaliknya
change_automatic_mode(change_by, val, time)
change_guest_mode(val)

#get
get_guest_mode()
get_automatic_mode()
get_electronics_room()
get_sensor_data()

#add
add_electronic_history(electronic_id, on, change_by, room, sensor_data, time)
add_automatic_mode_history(change_by, on, time)
add_home() -> sekali pakai
add_user(username, password, email, type)

#add_many
add_many_electronics(data)
add_many_room(data)
add_many_user_type(data)
add_many_user(data)
add_many_sensor(data)

#check pass
check_pass(user, passw)
'''


def home():
    con = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cur = con.cursor()
    cur.execute('''create table if not exists home(
        ID int,
        automatic_mode int,
        guest_mode int,
        unique(ID)
        )''')
    add_home()
    show('home')
    con.commit()
    con.close()


def user_type():
    con = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cur = con.cursor()
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS user_type (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            user_type char(8),
            change_guest_mode char(3),
            change_automatic_mode char(3),
            change_ac_mode char(3),
            change_music_mode char(3),
            change_lamp_mode char(3),
            send_email_username_password char(3),
            guest_mode_dependent char(3),
            automatic_mode_dependent char(3),
            unique(user_type)
            )''')
    con.commit()
    add_many_user_type([('Parent', 'YES', 'YES', 'YES', 'YES', 'YES', 'NO', 'NO', 'NO'), ('Children', 'NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'NO', 'YES'),
                        ('Admin', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO'), ('Guest', 'NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'YES', 'NO')])
    show('user_type')
    con.commit()
    con.close()


def user():
    con = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS user(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username text,
        password text,
        email text,
        user_type int,
        foreign key(user_type) references user_type(ID),
        unique(username)
    ) ''')
    add_many_user([('Petra Leka', 'Petra Ganteng', 'PetraOke@gmail.com', 1), ('Christianse Hemerli', 'All for Jesus', 'Sese@gmail.com', 2),
                   ('Marthin Chang', 'SayaWibu', 'makimalovers@gmail.com', 3), ('Pixel Christopher', 'buah apa paling receh? buah ha ha', 'pixel@gmail.com', 4), ('AI', 'ncdkslnjxzmcnsdfjnds84379q230ndaskA', 'none', 5)])
    show('user')
    con.commit()
    con.close()


def room():
    con = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cur = con.cursor()
    cur.execute('''create table if not exists room
(
	ID integer primary key autoincrement not null,
    room_type char(100),
    AC char(3),
    Music char(3),
    Lamp char(3),
    time_lamp_manual char(23),
    time_music_manual char(23),
    time_music_on char(23),
    unique(room_type)
)''')
    add_many_room([('Bedroom', 'YES', 'YES', 'YES', '22-06', '22-06', '08-11'), ('Kitchen', 'YES', 'YES', 'YES', '-1', '-1', '22-06'),
                   ('Bathroom', 'NO', 'YES', 'YES', '-1', '-1', '08-11'), ('Living Room', 'YES', 'YES', 'YES', '-1', '-1', '08-11')])
    show('room')
    con.commit()
    con.close()


def electronics():
    con = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cur = con.cursor()
    cur.execute('''create table if not exists electronics
(
	ID integer primary key autoincrement not null,
    name char(100),
    room_id int,
    on_off int,
    changed_by int,
    time_last_changed char(23),
    foreign key(room_id) references room(ID),
    unique(name)
)
''')
    add_many_electronics([('AC Bedroom', 1, 1, 5, '00'), ('AC kitchen', 2, 1, 5, '00'),
                          ('AC living room', 4, 1, 5, '00'),
                          ('Music Bedroom', 1, 1, 5,
                           '00'), ('Music kitchen', 2, 1, 5, '00'),
                          ('Music bathroom', 3, 1, 5,
                           '00'), ('Music living room', 4, 1, 5, '00'),
                          ('Lamp bedroom', 1, 1, 5,
                           '00'), ('Lamp kitchen', 2, 1, 5, '00'),
                          ('Lamp bathroom', 3, 1, 5, '00'), ('Lamp living room', 4, 1, 5, '00')])
    show('electronics')
    con.commit()
    con.close()


def sensor():
    con = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cur = con.cursor()
    cur.execute('''create table if not exists sensor(
        ID  integer primary key autoincrement not null,
        name char(100),
        id_room int,
        current_data char(10),
        unique(name)
        )''')
    add_many_sensor([('Sensor suhu bedroom', 1, '23'), ('Sensor suhu kitchen', 2, '24'),
                     ('Sensor suhu living room', 4, '26'), ('Sensor cahaya bedroom',
                                                            1, '30'), ('Sensor cahaya kitchen', 2, '35'),
                     ('Sensor cahaya bathroom', 3, '30'), ('Sensor cahaya living room',
                                                           4, '50'), ('Sensor orang bedroom', 1, '1'),
                     ('Sensor orang kitchen', 2, '1'), ('Sensor orang bathroom', 3, '1'), ('Sensor orang living room', 4, '1')])
    show('sensor')
    con.commit()
    con.close()


# add_many
def add_many_sensor(data):
    con = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cur = con.cursor()
    cur.executemany(
        'INSERT OR IGNORE INTO sensor VALUES(null, ?, ? , ?)', data)
    con.commit()
    con.close()


def add_many_electronics(data):
    c = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cr = c.cursor()
    cr.executemany(
        'INSERT OR IGNORE INTO electronics VALUES(null, ?, ?, ?, ?, ?)', data)
    c.commit()
    c.close()


def add_many_room(data):
    c = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cr = c.cursor()
    cr.executemany(
        'INSERT OR IGNORE INTO room VALUES(null, ?, ?, ?, ?, ?, ?, ?)', data)
    c.commit()
    c.close()


def add_many_user_type(data):
    c = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cr = c.cursor()
    cr.executemany(
        'INSERT OR IGNORE INTO user_type VALUES(null, ?, ?, ?, ?, ?, ?, ?, ?, ?)', data)
    c.commit()
    c.close()


def add_many_user(data):
    c = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cr = c.cursor()
    cr.executemany(
        'INSERT OR IGNORE INTO user VALUES(null, ?, ?, ?, ?)', data)
    c.commit()
    c.close()

# add


def add_user(username, password, email, type):
    c = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cr = c.cursor()
    cr.execute(
        'INSERT OR IGNORE INTO user VALUES(null, ?, ?, ?, ?)', (username, password, email, type))
    c.commit()
    c.close()


def add_home():
    con = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cur = con.cursor()
    cur.execute(
        'insert or ignore into home(ID, automatic_mode, guest_mode) values(1, {auto}, {guest})'.format(auto=1, guest=1))
    con.commit()
    con.close()


def add_automatic_mode_history(change_by, on, time):
    con = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cur = con.cursor()
    cur.execute(
        'insert into automatic_mode_history values(null, ?, ?, ?)', (change_by, on, time))
    con.commit()
    con.close()


# get


# history


def electronics_history():
    con = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cur = con.cursor()
    cur.execute('''create table if not exists electronics_history(
        ID integer primary key autoincrement not null,
        electronic_id int,
        on_off int,
        changed_by int,
        room char(100),
        sensor_data char(10),
        time char(23),
        foreign key(changed_by) references user(ID),
        foreign key(room) references room(room_type)
        )''')
    # add_many_electronics_history([])
    show('electronics_history')
    con.commit()
    con.close()


def guest_mode_history():
    con = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cur = con.cursor()
    cur.execute('''create table if not exists guest_mode_history(
        ID integer primary key autoincrement not null,
        changed_by int,
        on_off int,
        time char(23),
        foreign key(changed_by) references user(ID)
        )
        ''')
    # add_automatic_mode_history([])
    con.commit()
    con.close()
    show('guest_mode_history')


def automatic_mode_history():
    con = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cur = con.cursor()
    cur.execute('''create table if not exists automatic_mode_history(
        ID integer primary key autoincrement not null,
        changed_by int,
        on_off int,
        time char(23),
        foreign key(changed_by) references user(ID)
        )
        ''')
    # add_automatic_mode_history([])
    con.commit()
    con.close()
    show('automatic_mode_history')


def show(table):
    c = sql.connect(
        'C:\kuliah\semester 3\Pemrograman berbasis objek IoT\project_smart_home\smarthome.db')
    cor = c.cursor()
    cor.execute('SELECT * FROM {tabel}'.format(tabel=table))
    print(cor.fetchall(), 'done')
    c.commit()
    c.close()


def delete(id):
    c = sql.connect('data.db')
    cr = c.cursor()
    cr.execute('DELETE FROM customers WHERE rowid = id')
    c.commit()
    c.close()


def main():
    user_type()
    user()
    room()
    electronics()
    electronics_history()
    sensor()
    automatic_mode_history()
    home()
    guest_mode_history()


def test():
    # main table
    home()
    user_type()
    user()
    room()
    electronics()
    sensor()

    change_by = 1
    on = 0
    time = '01'
    add_automatic_mode_history(change_by, on, time)
    # add_home() -> sekali pakai
    #add_user(username, password, email, type)

    # add_many
    '''
    add_many_electronics(data)
    add_many_room(data)
    add_many_user_type(data)
    add_many_user(data)
    add_many_sensor(data)'''

    # history
    electronics_history()
    automatic_mode_history()


if __name__ == '__main__':
    main()
    # test()
    # guest_mode_history()
