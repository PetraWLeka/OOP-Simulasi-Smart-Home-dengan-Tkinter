'''
list fungsi:

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


#check pass
check_pass(user, passw)

#automatic control
automatic_control()

#thread untuk update data sensor terus menerus
thrd()
'''
import sensor as sns
import sqlite3 as sql
import time
import threading
#import GUI as ui

# add


def add_electronic_history(electronic_id, on, change_by, room, sensor_data, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('insert into electronics_history values(null, ?, ?, ?, ?, ?, ?)',
                (electronic_id, on, change_by, room, sensor_data, time))
    con.commit()
    con.close()


def add_automatic_mode_history(change_by, on, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'insert into automatic_mode_history values(null, ?, ?, ?)', (change_by, on, time))
    con.commit()
    con.close()


def add_guest_mode_history(change_by, on, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'insert into guest_mode_history values(null, ?, ?, ?)', (change_by, on, time))
    con.commit()
    con.close()

# get


def get_user_type(username):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select user_type from user where username = "{}"'.format(
        username))
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


def get_guest_mode():
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select guest_mode from home where ID = 1')
    data = cur.fetchone()[0]
    # print(data)
    con.commit()
    con.close()
    return data


def get_automatic_mode():
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select automatic_mode from home where ID = 1')
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


def get_ac_bedroom():
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select on_off from electronics where name = "AC Bedroom"')
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


def get_ac_living_room():
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select on_off from electronics where name = "AC living room"')
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


def get_ac_kitchen():
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select on_off from electronics where name = "AC kitchen"')
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


def get_lamp_bedroom():
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select on_off from electronics where name = "Lamp bedroom"')
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


def get_lamp_bathroom():
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select on_off from electronics where name = "Lamp bathroom"')
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


def get_lamp_living_room():
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select on_off from electronics where name = "Lamp living room"')
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


def get_lamp_kitchen():
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select on_off from electronics where name = "Lamp kitchen"')
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


def get_music_bedroom():
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select on_off from electronics where name = "Music Bedroom"')
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


def get_music_kitchen():
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select on_off from electronics where name = "Music kitchen"')
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


def get_music_bathroom():
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select on_off from electronics where name = "Music bathroom"')
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


def get_music_living_room():
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'select on_off from electronics where name = "Music living room"')
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


def get_sensor_data(id):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('select current_data from sensor where ID = ?', (id,))
    data = cur.fetchone()[0]
    con.commit()
    con.close()
    return data


# change
def change_automatic_mode(change_by, val, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('update home set automatic_mode = ? where ID = 1', (val,))
    con.commit()
    con.close()
    add_automatic_mode_history(change_by, val, time)


def change_guest_mode(change_by, val, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute('update home set guest_mode = ? where ID = 1', (val,))
    con.commit()
    con.close()
    add_guest_mode_history(change_by, val, time)


def change_ac_bedroom(val, user, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'update electronics set on_off = ?, changed_by = ?, time_last_changed = ? where ID = 1', (val, user, time))
    data = get_sensor_data(1)
    con.commit()
    con.close()
    add_electronic_history(1, val, user, 1, data, time)


def change_ac_living_room(val, user, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'update electronics set on_off = ?, changed_by = ?, time_last_changed = ? where ID = 3', (val, user, time))
    data = get_sensor_data(3)
    con.commit()
    con.close()
    add_electronic_history(4, val, user, 4, data, time)


def change_ac_kitchen(val, user, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'update electronics set on_off = ?, changed_by = ?, time_last_changed = ? where ID = 2', (val, user, time))
    data = get_sensor_data(2)
    con.commit()
    con.close()
    add_electronic_history(2, val, user, 2, data, time)


def change_lamp_bedroom(val, user, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'update electronics set on_off = ?, changed_by = ?, time_last_changed = ? where ID = 8', (val, user, time))
    data = get_sensor_data(4)
    con.commit()
    con.close()
    add_electronic_history(8, val, user, 1, data, time)


def change_lamp_bathroom(val, user, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'update electronics set on_off = ?, changed_by = ?, time_last_changed = ? where ID = 10', (val, user, time))
    data = get_sensor_data(6)
    con.commit()
    con.close()
    add_electronic_history(10, val, user, 3, data, time)


def change_lamp_living_room(val, user, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'update electronics set on_off = ?, changed_by = ?, time_last_changed = ? where ID = 11', (val, user, time))
    data = get_sensor_data(7)
    con.commit()
    con.close()
    add_electronic_history(11, val, user, 4, data, time)


def change_lamp_kitchen(val, user, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'update electronics set on_off = ?, changed_by = ?, time_last_changed = ? where ID = 9', (val, user, time))
    data = get_sensor_data(5)
    con.commit()
    con.close()
    add_electronic_history(9, val, user, 2, data, time)


def change_music_bedroom(val, user, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'update electronics set on_off = ?, changed_by = ?, time_last_changed = ? where ID = 4', (val, user, time))
    data = get_sensor_data(8)
    con.commit()
    con.close()
    add_electronic_history(4, val, user, 1, data, time)


def change_music_kitchen(val, user, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'update electronics set on_off = ?, changed_by = ?, time_last_changed = ? where ID = 5', (val, user, time))
    data = get_sensor_data(9)
    con.commit()
    con.close()
    add_electronic_history(5, val, user, 2, data, time)


def change_music_bathroom(val, user, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'update electronics set on_off = ?, changed_by = ?, time_last_changed = ? where ID = 6', (val, user, time))
    data = get_sensor_data(10)
    con.commit()
    con.close()
    add_electronic_history(6, val, user, 3, data, time)


def change_music_living_room(val, user, time):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'update electronics set on_off = ?, changed_by = ?, time_last_changed = ? where ID = 7', (val, user, time))
    data = get_sensor_data(11)
    con.commit()
    con.close()
    add_electronic_history(7, val, user, 4, data, time)


def change_sensor(ID, data):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'update sensor set current_data = {d} where ID = {id}'.format(d=data, id=ID))
    con.commit()
    con.close()


def change_pass(username, new_pass):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute("update user set password = '{passw}' where username = '{name}'".format(
        passw=new_pass, name=username))
    con.commit()
    con.close()

# check pass


def check_pass(username, passw):
    con = sql.connect(
        'smarthome.db')
    cur = con.cursor()
    cur.execute(
        'select password from user where username = "{name}"'.format(name=username))
    try:
        if cur.fetchone()[0] == passw:
            con.commit()
            con.close()
            return True
        else:
            con.commit()
            con.close()
            return False
    except:
        con.commit()
        con.close()
        return False


# automatic_control


def automatic_control():
    suhu = sns.all_suhu()
    cahaya = sns.all_cahaya()
    orang = sns.all_orang()
    electronics = []
    i = 0
    for sh in suhu:
        if i == 2:
            i = 3
        if sh > 32 and orang[i] > 0:
            electronics.append("ON")
        else:
            electronics.append("OFF")
        i += 1
    i = 0
    for ch in cahaya:

        if ch < 150 and orang[i] > 0:
            electronics.append("ON")
        else:
            electronics.append("OFF")
    for org in orang:
        if org > 0:
            electronics.append("ON")
        else:
            electronics.append("OFF")
    return electronics  # sns.suhu_bedroom, sns.suhu_kitchen, sns.suhu_living_room,
    #sns.cahaya_bedroom, sns.cahaya_kitchen, sns.cahaya_bathroom, sns.cahaya_living_room
    #sns.orang_bedroom, sns.orang_kitchen, sns.orang_bathroom, sns.orang_living_room


# threading sensor
loop_thrd = True


def thrd():
    while loop_thrd:
        sh = sns.all_suhu()
        ch = sns.all_cahaya()
        org = sns.all_orang()

        change_sensor(1, sh[0])
        change_sensor(2, sh[1])
        change_sensor(3, sh[2])

        change_sensor(4, ch[0])
        change_sensor(5, ch[1])
        change_sensor(6, ch[2])
        change_sensor(7, ch[3])

        change_sensor(8, org[0])
        change_sensor(9, org[1])
        change_sensor(10, org[2])
        change_sensor(11, org[3])
        time.sleep(1)


thread_sensor = threading.Thread(target=thrd, name="thread sensor", args=())
thread_sensor.start()
