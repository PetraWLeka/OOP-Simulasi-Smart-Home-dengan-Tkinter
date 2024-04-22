'''
daftar
class:
Login

method:
get_user_passw()
login()

fungsi:
children_auto()
parent_auto()
parent()
children()
guest()
admin()

time() untuk urus jam yang berubah tiap detik

parent_manu_to_auto(root)
parent_auto_to_manu(root)
guest_auto() == children_auto()


'''
from tkinter import *
from tkinter import ttk
from time import strftime
from time import localtime
from time import sleep
import API as api


class Login:
    def __init__(self):
        self.root = Tk()
        self.username = StringVar()
        self.password = StringVar()

    def get_user_passw(self):
        user = self.username.get()
        passw = self.password.get()
        print(user, passw, 'user passw\n')
        check = api.check_pass(user, passw)
        print(check, 'check')
        if check == True:
            type = api.get_user_type(user)
            self.root.destroy()
            aut = api.get_automatic_mode()
            if type == 1:
                if aut == 1:
                    parent_auto()
                else:
                    parent()
            elif type == 2:
                if aut == 1:
                    children_auto()
                else:
                    children()
            elif type == 3:
                admin()
            elif type == 4:
                if api.get_guest_mode() == 0:
                    guest_auto()
                else:
                    guest()

    def login(self):
        self.root.geometry("350x200")
        self.root.title("My Smart Home")
        login_info = Label(self.root, text="My Smart Home",
                           font=("Helvatica", 20, "bold"))
        login_info.grid(row=1, column=2, sticky=N)

        user = Label(self.root, text="Username")
        user.grid(row=3, column=1, pady=10, sticky=W)

        userentry = Entry(self.root, textvariable=self.username,  width=30)
        userentry.grid(row=3, column=2, pady=5)

        passw = Label(self.root, text="Password")
        passw.grid(row=4, column=1, pady=5, sticky=W)
        passwentry = Entry(self.root, textvariable=self.password,
                           show="*", width=30)
        passwentry.grid(row=4, column=2, pady=5)

        login = Button(self.root, command=self.get_user_passw, text="Login")
        login.grid(row=5, column=2, pady=5, sticky=N)

        not_yet = Label(self.root, text='Not yet logged in!')
        not_yet.grid(row=6, column=2, sticky=N)

        self.root.mainloop()


def children_auto():
    api.loop_thrd = True
    root = Tk()
    root.geometry("450x600")
    root.title("My Smart Home")
    login_info = Label(root, text="My Smart Home",
                       font=("Helvatica", 20, "bold"))
    login_info.place(x=100, y=1)

    def time():
        named_tuple = localtime()  # get struct_time
        time_string = str(
            int(strftime("%S", named_tuple)) % 24)
        lbl.config(text=time_string)
        lbl.after(1000, time)

    lbl = Label(root, font=('calibri', 20, 'bold'),
                background='white', foreground='black')
    lbl.place(x=125, y=215)

    Room_1 = Label(root, text="Bedroom")
    Room_1.place(x=1, y=60)

    AC = Label(root, text="AC", )
    AC.place(x=20, y=80)
    on_ac_1 = StringVar()
    on_ac_3 = StringVar()
    on_ac_4 = StringVar()
    on_lampu_1 = StringVar()
    on_lampu_2 = StringVar()
    on_lampu_3 = StringVar()
    on_lampu_4 = StringVar()
    on_musik_1 = StringVar()
    on_musik_2 = StringVar()
    on_musik_3 = StringVar()
    on_musik_4 = StringVar()
    if api.get_ac_bedroom() == 1:
        on_ac_1.set("ON")
    else:
        on_ac_1.set("OFF")

    if api.get_lamp_bedroom() == 1:
        on_lampu_1.set("ON")
    else:
        on_lampu_1.set("OFF")

    if api.get_music_bedroom() == 1:
        on_musik_1.set("ON")
    else:
        on_musik_1.set("OFF")

    if api.get_lamp_bathroom() == 1:
        on_lampu_2.set("ON")
    else:
        on_lampu_2.set("OFF")

    if api.get_music_bathroom() == 1:
        on_musik_2.set("ON")
    else:
        on_musik_2.set("OFF")

    if api.get_ac_living_room() == 1:
        on_ac_3.set("ON")
    else:
        on_ac_3.set("OFF")

    if api.get_lamp_living_room() == 1:
        on_lampu_3.set("ON")
    else:
        on_lampu_3.set("OFF")

    if api.get_music_living_room() == 1:
        on_musik_3.set("ON")
    else:
        on_musik_3.set("OFF")

    if api.get_ac_kitchen() == 1:
        on_ac_4.set("ON")
    else:
        on_ac_4.set("OFF")

    if api.get_lamp_kitchen() == 1:
        on_lampu_4.set("ON")
    else:
        on_lampu_4.set("OFF")

    if api.get_music_kitchen() == 1:
        on_musik_4.set("ON")
    else:
        on_musik_4.set("OFF")

    # room_1_ac_off

    room_1_ac_on = Label(root, textvariable=on_ac_1)
    room_1_ac_on.place(x=19, y=100)

    Lampu = Label(root, text='Lampu')
    Lampu.place(x=65, y=80)

    # room_1_lampu_off

    room_1_lampu_on = Label(root, textvariable=on_lampu_1)
    room_1_lampu_on.place(x=75, y=100)

    musik = Label(root, text="Musik")
    musik.place(x=125, y=80)

    # room_1_musik_off

    room_1_musik_on = Label(root, textvariable=on_musik_1)
    room_1_musik_on.place(x=130, y=100)

    Room_2 = Label(root, text="Bathroom")
    Room_2.place(x=1, y=130)

    Lampu2 = Label(root, text='Lampu')
    Lampu2.place(x=10, y=150)

    # room_2_lampu_off

    room_2_lampu_on = Label(root, textvariable=on_lampu_2)
    room_2_lampu_on.place(x=20, y=170)

    musik2 = Label(root, text="Musik")
    musik2.place(x=65, y=150)

    # room_2_musik_off

    room_2_musik_on = Label(root, textvariable=on_musik_2)
    room_2_musik_on.place(x=70, y=170)

    Room_3 = Label(root, text="Living Room")
    Room_3.place(x=270, y=60)

    AC3 = Label(root, text="AC")
    AC3.place(x=280, y=80)

    # room_3_AC_off

    room_3_AC_on = Label(root, textvariable=on_ac_3)
    room_3_AC_on.place(x=280, y=100)

    Lampu = Label(root, text='Lampu')
    Lampu.place(x=325, y=80)

    # room_3_lampu_off

    room_3_lampu_on = Label(root, textvariable=on_lampu_3)
    room_3_lampu_on.place(x=335, y=100)

    musik = Label(root, text="Musik")
    musik.place(x=390, y=80)

    # room_3_musik_off

    room_3_musik_on = Label(root, textvariable=on_musik_3)
    room_3_musik_on.place(x=396, y=100)

    Room_4 = Label(root, text="Kitchen")
    Room_4.place(x=270, y=130)

    AC4 = Label(root, text="AC")
    AC4.place(x=280, y=150)

    # room_4_ac_off

    room_4_ac_on = Label(root, textvariable=on_ac_4)
    room_4_ac_on.place(x=280, y=170)

    Lampu4 = Label(root, text='Lampu')
    Lampu4.place(x=325, y=150)

    # room_4_lampu_off

    room_4_lampu_on = Label(root, textvariable=on_lampu_4)
    room_4_lampu_on.place(x=335, y=170)

    musik4 = Label(root, text="Musik")
    musik4.place(x=390, y=150)

    # room_4_musik_off

    room_4_musik_on = Label(root, textvariable=on_musik_4)
    room_4_musik_on.place(x=396, y=170)

    time()

    def f():
        state = api.automatic_control()
        # sns.suhu_bedroom, sns.suhu_kitchen, sns.suhu_living_room,
    #sns.cahaya_bedroom, sns.cahaya_kitchen, sns.cahaya_bathroom, sns.cahaya_living_room
    #sns.orang_bedroom, sns.orang_kitchen, sns.orang_bathroom, sns.orang_living_room

        def g(state_):
            if state_ == "ON":
                return 1
            return 0
        on_ac_1.set(state[0])
        # on_ac_1.set("TES")
        on_lampu_1.set(state[3])
        on_musik_1.set(state[7])
        on_lampu_2.set(state[5])
        on_musik_2.set(state[9])
        on_ac_3.set(state[2])
        on_lampu_3.set(state[6])
        on_musik_3.set(state[10])
        on_ac_4.set(state[1])
        on_lampu_4.set(state[4])
        on_musik_4.set(state[8])
        # root.update_idletasks()
        # sleep(10)
        api.change_ac_bedroom(g(state[0]), 5, str(
            int(strftime("%S", localtime())) % 24) + ":00:00")
        api.change_lamp_bedroom(g(state[3]), 5, str(
            int(strftime("%S", localtime())) % 24) + ":00:00")
        api.change_music_bedroom(g(state[7]), 5, str(
            int(strftime("%S", localtime())) % 24) + ":00:00")
        api.change_lamp_bathroom(g(state[5]), 5, str(
            int(strftime("%S", localtime())) % 24) + ":00:00")
        api.change_music_bathroom(g(state[9]), 5, str(
            int(strftime("%S", localtime())) % 24) + ":00:00")
        api.change_ac_living_room(g(state[2]), 5, str(
            int(strftime("%S", localtime())) % 24) + ":00:00")
        api.change_lamp_living_room(g(state[6]), 5, str(
            int(strftime("%S", localtime())) % 24) + ":00:00")
        api.change_music_living_room(g(state[10]), 5, str(
            int(strftime("%S", localtime())) % 24) + ":00:00")
        api.change_ac_kitchen(g(state[1]), 5, str(
            int(strftime("%S", localtime())) % 24) + ":00:00")
        api.change_lamp_kitchen(g(state[4]), 5, str(
            int(strftime("%S", localtime())) % 24) + ":00:00")
        api.change_music_kitchen(g(state[8]), 5, str(
            int(strftime("%S", localtime())) % 24) + ":00:00")
        state.clear()
        data = int(strftime("%S", localtime())) % 24
        if data >= 8 and data <= 11:
            on_musik_1.set("ON")
            on_musik_2.set("ON")
            on_musik_3.set("ON")
            on_musik_4.set("ON")
        if data >= 22 or data <= 6:
            on_lampu_1.set("OFF")
            on_musik_1.set("OFF")
        root.after(1000, f)
    f()
    root.mainloop()
    api.loop_thrd = True


def parent_auto():
    api.loop_thrd = True

    root = Tk()
    root.geometry("450x600")
    root.title("My Smart Home")
    login_info = Label(root, text="My Smart Home",
                       font=("Helvatica", 20, "bold"))
    login_info.grid(row=1, column=2, sticky=N)
    guest = Label(root, text="Guest Mode")
    guest.grid(row=2, column=1, sticky=W)

    var = IntVar()
    var.set(api.get_guest_mode())
    #print(var.get(), api.get_guest_mode())

    guest_on = Radiobutton(root, text="ON", variable=var,
                           command=lambda: api.change_guest_mode(1, var.get(), str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), value=1)
    guest_on.grid(row=3, column=1, sticky=W)

    guest_off = Radiobutton(root, text="OFF", variable=var,
                            command=lambda: api.change_guest_mode(1, var.get(), str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), value=0)
    guest_off.grid(row=4, column=1, sticky=W)

    auto = Label(root, text="Automatic Mode")
    auto.grid(row=2, column=3, pady=5, sticky=W)

    var1 = IntVar()
    var1.set(api.get_automatic_mode())

    autobtn = Radiobutton(root, text="Automatic", command=lambda: api.change_automatic_mode(
        1, var1.get(), str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var1, value=1)
    autobtn.grid(row=3, column=3, sticky=W)

    manubtn = Radiobutton(root, text="Manual", command=lambda: [api.change_automatic_mode(
        1, var1.get(), str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), parent_auto_to_manu(root)], variable=var1,  value=0)
    manubtn.grid(row=4, column=3, sticky=W)

    def time():
        named_tuple = localtime()  # get struct_time
        time_string = str(
            int(strftime("%S", named_tuple)) % 24)
        lbl.config(text=time_string)
        lbl.after(1000, time)

    lbl = Label(root, font=('times new roman', 20, 'bold'),
                background='white', foreground='black')
    lbl.place(x=125, y=335)

    breakline2 = ttk.Separator(root, orient='horizontal')
    breakline2.grid(row=8, columnspan=100, ipadx=250, pady=10)
    on_ac_1 = StringVar()
    on_ac_3 = StringVar()
    on_ac_4 = StringVar()
    on_lampu_1 = StringVar()
    on_lampu_2 = StringVar()
    on_lampu_3 = StringVar()
    on_lampu_4 = StringVar()
    on_musik_1 = StringVar()
    on_musik_2 = StringVar()
    on_musik_3 = StringVar()
    on_musik_4 = StringVar()
    if api.get_ac_bedroom() == 1:
        on_ac_1.set("ON")
    else:
        on_ac_1.set("OFF")

    if api.get_lamp_bedroom() == 1:
        on_lampu_1.set("ON")
    else:
        on_lampu_1.set("OFF")

    if api.get_music_bedroom() == 1:
        on_musik_1.set("ON")
    else:
        on_musik_1.set("OFF")

    if api.get_lamp_bathroom() == 1:
        on_lampu_2.set("ON")
    else:
        on_lampu_2.set("OFF")

    if api.get_music_bathroom() == 1:
        on_musik_2.set("ON")
    else:
        on_musik_2.set("OFF")

    if api.get_ac_living_room() == 1:
        on_ac_3.set("ON")
    else:
        on_ac_3.set("OFF")

    if api.get_lamp_living_room() == 1:
        on_lampu_3.set("ON")
    else:
        on_lampu_3.set("OFF")

    if api.get_music_living_room() == 1:
        on_musik_3.set("ON")
    else:
        on_musik_3.set("OFF")

    if api.get_ac_kitchen() == 1:
        on_ac_4.set("ON")
    else:
        on_ac_4.set("OFF")

    if api.get_lamp_kitchen() == 1:
        on_lampu_4.set("ON")
    else:
        on_lampu_4.set("OFF")

    if api.get_music_kitchen() == 1:
        on_musik_4.set("ON")
    else:
        on_musik_4.set("OFF")

    Room_1 = Label(root, text="Bedroom")
    Room_1.place(x=1, y=130)

    AC = Label(root, text="AC", )
    AC.place(x=20, y=150)

    # room_1_ac_off

    room_1_ac_on = Label(root, textvariable=on_ac_1)
    room_1_ac_on.place(x=19, y=170)

    Lampu = Label(root, text='Lampu')
    Lampu.place(x=65, y=150)

    # room_1_lampu_off

    room_1_lampu_on = Label(root, textvariable=on_lampu_1)
    room_1_lampu_on.place(x=75, y=170)

    musik = Label(root, text="Musik")
    musik.place(x=125, y=150)

    # room_1_musik_off

    room_1_musik_on = Label(root, textvariable=on_musik_1)
    room_1_musik_on.place(x=130, y=170)

    Room_2 = Label(root, text="Bathroom")
    Room_2.place(x=1, y=220)

    Lampu2 = Label(root, text='Lampu')
    Lampu2.place(x=10, y=240)

    # room_2_lampu_off

    room_2_lampu_on = Label(root, textvariable=on_lampu_2)
    room_2_lampu_on.place(x=20, y=260)

    musik2 = Label(root, text="Musik")
    musik2.place(x=65, y=240)

    # room_2_musik_off

    room_2_musik_on = Label(root, textvariable=on_musik_2)
    room_2_musik_on.place(x=70, y=260)

    Room_3 = Label(root, text="Living Room")
    Room_3.place(x=270, y=130)

    AC3 = Label(root, text="AC")
    AC3.place(x=280, y=150)

    # room_3_AC_off

    room_3_AC_on = Label(root, textvariable=on_ac_3)
    room_3_AC_on.place(x=280, y=170)

    Lampu = Label(root, text='Lampu')
    Lampu.place(x=325, y=150)

    # room_3_lampu_off

    room_3_lampu_on = Label(root, textvariable=on_lampu_3)
    room_3_lampu_on.place(x=335, y=170)

    musik = Label(root, text="Musik")
    musik.place(x=390, y=150)

    # room_3_musik_off

    room_3_musik_on = Label(root, textvariable=on_musik_3)
    room_3_musik_on.place(x=396, y=170)

    Room_4 = Label(root, text="Kitchen")
    Room_4.place(x=270, y=220)

    AC4 = Label(root, text="AC")
    AC4.place(x=280, y=240)

    # room_4_ac_off

    room_4_ac_on = Label(root, textvariable=on_ac_4)
    room_4_ac_on.place(x=280, y=260)

    Lampu4 = Label(root, text='Lampu')
    Lampu4.place(x=325, y=240)

    # room_4_lampu_off

    room_4_lampu_on = Label(root, textvariable=on_lampu_4)
    room_4_lampu_on.place(x=335, y=260)

    musik4 = Label(root, text="Musik")
    musik4.place(x=390, y=240)

    # room_4_musik_off

    room_4_musik_on = Label(root, textvariable=on_musik_4)
    room_4_musik_on.place(x=396, y=260)

    time()
    # root.mainloop()

    def f():
        state = api.automatic_control()
        # sns.suhu_bedroom, sns.suhu_kitchen, sns.suhu_living_room,
    #sns.cahaya_bedroom, sns.cahaya_kitchen, sns.cahaya_bathroom, sns.cahaya_living_room
    #sns.orang_bedroom, sns.orang_kitchen, sns.orang_bathroom, sns.orang_living_room
        on_ac_1.set(state[0])
        # on_ac_1.set("TES")
        on_lampu_1.set(state[3])
        on_musik_1.set(state[7])
        on_lampu_2.set(state[5])
        on_musik_2.set(state[9])
        on_ac_3.set(state[2])
        on_lampu_3.set(state[6])
        on_musik_3.set(state[10])
        on_ac_4.set(state[1])
        on_lampu_4.set(state[4])
        on_musik_4.set(state[8])
        if state[0] == "ON":
            q = 1
        else:
            q = 0
        if state[3] == "ON":
            w = 1
        else:
            w = 0
        if state[7] == "ON":
            e = 1
        else:
            e = 0
        if state[5] == "ON":
            r = 1
        else:
            r = 0
        if state[9] == "ON":
            t = 1
        else:
            t = 0
        if state[2] == "ON":
            y = 1
        else:
            y = 0
        if state[6] == "ON":
            u = 1
        else:
            u = 0
        if state[10] == "ON":
            o = 1
        else:
            o = 0
        if state[1] == "ON":
            p = 1
        else:
            p = 0
        if state[4] == "ON":
            a = 1
        else:
            a = 0
        if state[8] == "ON":
            s = 1
        else:
            s = 0

        api.change_ac_bedroom(
            q, 5, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00")
        api.change_lamp_bedroom(
            w, 5, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00")
        api.change_music_bedroom(
            e, 5, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00")
        api.change_lamp_bathroom(
            r, 5, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00")
        api.change_music_bathroom(
            t, 5, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00")
        api.change_ac_living_room(
            y, 5, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00")
        api.change_lamp_living_room(
            u, 5, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00")
        api.change_music_living_room(
            o, 5, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00")
        api.change_ac_kitchen(
            p, 5, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00")
        api.change_lamp_kitchen(
            a, 5, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00")
        api.change_music_kitchen(
            s, 5, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00")

        # root.update_idletasks()
        # sleep(10)
        state.clear()
        time = int(strftime("%S", localtime())) % 24
        if time >= 8 and time <= 11:
            on_musik_1.set("ON")
            on_musik_2.set("ON")
            on_musik_3.set("ON")
            on_musik_4.set("ON")
        if time >= 22 or time <= 6:
            on_lampu_1.set("OFF")
            on_musik_1.set("OFF")
        root.after(1000, f)
    f()

    root.mainloop()
    api.loop_thrd = False


def parent():
    api.loop_thrd = True

    root = Tk()
    root.geometry("450x500")
    root.title("My Smart Home")
    login_info = Label(root, text="My Smart Home",
                       font=("Helvatica", 20, "bold"))
    login_info.grid(row=1, column=2, sticky=N)

    guest = Label(root, text="Guest Mode")
    guest.grid(row=2, column=1, sticky=W)

    var = IntVar()
    var.set(api.get_guest_mode())
    #print(var.get(), api.get_guest_mode())

    guest_on = Radiobutton(root, text="ON", variable=var,
                           command=lambda: api.change_guest_mode(1, var.get(), str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), value=1)
    guest_on.grid(row=3, column=1, sticky=W)

    guest_off = Radiobutton(root, text="OFF", variable=var,
                            command=lambda: api.change_guest_mode(1, var.get(), str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), value=0)
    guest_off.grid(row=4, column=1, sticky=W)

    auto = Label(root, text="Automatic Mode")
    auto.grid(row=5, column=1, pady=5, sticky=W)

    var1 = IntVar()
    var1.set(api.get_automatic_mode())

    autobtn = Radiobutton(root, text="Automatic", command=lambda: [api.change_automatic_mode(
        1, var1.get(), str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), parent_manu_to_auto(root)], variable=var1, value=1)
    autobtn.grid(row=6, column=1, sticky=W)

    manubtn = Radiobutton(root, text="Manual", command=lambda: api.change_automatic_mode(
        1, var1.get(), str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var1,  value=0)
    manubtn.grid(row=7, column=1, sticky=W)

    def time():
        named_tuple = localtime()  # get struct_time
        time_string = str(
            int(strftime("%S", named_tuple)) % 24)
        lbl.config(text=time_string)
        lbl.after(1000, time)

    lbl = Label(root, font=('times new roman', 20, 'bold'),
                background='white', foreground='black')
    lbl.place(x=200, y=85)

    breakline2 = ttk.Separator(root, orient='horizontal')
    breakline2.grid(row=8, columnspan=100, ipadx=250, pady=10)

    Room_1 = Label(root, text="Bedroom")
    Room_1.place(x=1, y=190)

    AC = Label(root, text="AC", )
    AC.place(x=20, y=210)

    var2 = IntVar()
    var2.set(api.get_ac_bedroom())

    room_1_ac_on = Radiobutton(root, text="ON", command=lambda: api.change_ac_bedroom(
        var2.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var2, value=1)
    room_1_ac_on.place(x=1, y=230)

    room_1_ac_off = Radiobutton(root, text="OFF", command=lambda: api.change_ac_bedroom(
        var2.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var2,  value=0)
    room_1_ac_off.place(x=1, y=250)

    Lampu = Label(root, text='Lampu')
    Lampu.place(x=65, y=210)

    var3 = IntVar()
    var3.set(api.get_lamp_bedroom())

    room_1_lamp_on = Radiobutton(root, text="ON", command=lambda: api.change_lamp_bedroom(
        var3.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var3, value=1)
    room_1_lamp_on.place(x=60, y=230)

    room_1_lamp_off = Radiobutton(root, text="OFF", command=lambda: api.change_lamp_bedroom(
        var3.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var3,  value=0)
    room_1_lamp_off.place(x=60, y=250)

    musik = Label(root, text="Musik")
    musik.place(x=125, y=210)

    var4 = IntVar()
    var4.set(api.get_music_bedroom())

    room_1_musik_on = Radiobutton(root, text="ON", command=lambda: api.change_music_bedroom(
        var4.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var4, value=1)
    room_1_musik_on.place(x=120, y=230)

    room_1_musik_off = Radiobutton(root, text="OFF", command=lambda: api.change_music_bedroom(
        var4.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var4,  value=0)
    room_1_musik_off.place(x=120, y=250)

    Room_2 = Label(root, text="Bathroom")
    Room_2.place(x=1, y=280)

    Lampu2 = Label(root, text='Lampu')
    Lampu2.place(x=10, y=300)

    lamp2 = IntVar()
    lamp2.set(api.get_lamp_bathroom())

    room_2_lamp_on = Radiobutton(root, text="ON", command=lambda: api.change_lamp_bathroom(
        lamp2.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp2, value=1)
    room_2_lamp_on.place(x=1, y=320)

    room_2_lamp_off = Radiobutton(root, text="OFF", command=lambda: api.change_lamp_bathroom(
        lamp2.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp2,  value=0)
    room_2_lamp_off.place(x=1, y=340)

    musik2 = Label(root, text="Musik")
    musik2.place(x=65, y=300)

    mus2 = IntVar()
    mus2.set(api.get_music_bathroom())

    room_2_musik_on = Radiobutton(root, text="ON", command=lambda: api.change_music_bathroom(
        mus2.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus2, value=1)
    room_2_musik_on.place(x=60, y=320)

    room_2_musik_off = Radiobutton(root, text="OFF", command=lambda: api.change_music_bathroom(
        mus2.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus2,  value=0)
    room_2_musik_off.place(x=60, y=340)

    Room_3 = Label(root, text="Living Room")
    Room_3.place(x=270, y=190)

    AC3 = Label(root, text="AC")
    AC3.place(x=280, y=210)

    ac3 = IntVar()
    ac3.set(api.get_ac_living_room())

    room_3_ac_on = Radiobutton(root, text="ON", command=lambda: api.change_ac_living_room(
        ac3.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=ac3, value=1)
    room_3_ac_on.place(x=265, y=230)

    room_3_ac_off = Radiobutton(root, text="OFF", command=lambda: api.change_ac_living_room(
        ac3.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"),  variable=ac3,  value=0)
    room_3_ac_off.place(x=265, y=250)

    Lampu = Label(root, text='Lampu')
    Lampu.place(x=325, y=210)

    lamp3 = IntVar()
    lamp3.set(api.get_lamp_living_room())

    room_3_lamp_on = Radiobutton(root, text="ON", command=lambda: api.change_lamp_living_room(
        lamp3.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp3, value=1)
    room_3_lamp_on.place(x=320, y=230)

    room_3_lamp_off = Radiobutton(root, text="OFF", command=lambda: api.change_lamp_living_room(
        lamp3.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp3,  value=0)
    room_3_lamp_off.place(x=320, y=250)

    musik = Label(root, text="Musik")
    musik.place(x=390, y=210)

    mus3 = IntVar()
    mus3.set(api.get_music_living_room())

    room_3_musik_on = Radiobutton(root, text="ON", command=lambda: api.change_music_living_room(
        mus3.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus3, value=1)
    room_3_musik_on.place(x=385, y=230)

    room_3_musik_off = Radiobutton(root, text="OFF", command=lambda: api.change_music_living_room(
        mus3.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"),  variable=mus3,  value=0)
    room_3_musik_off.place(x=385, y=250)
    Room_4 = Label(root, text="Kitchen")
    Room_4.place(x=270, y=280)

    AC4 = Label(root, text="AC")
    AC4.place(x=280, y=300)

    ac4 = IntVar()
    ac4.set(api.get_ac_kitchen())

    room_4_ac_on = Radiobutton(root, text="ON", command=lambda: api.change_ac_kitchen(
        ac4.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=ac4, value=1)
    room_4_ac_on.place(x=265, y=320)

    room_4_ac_off = Radiobutton(root, text="OFF", command=lambda: api.change_ac_kitchen(
        ac4.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=ac4,  value=0)
    room_4_ac_off.place(x=265, y=340)

    Lampu4 = Label(root, text='Lampu')
    Lampu4.place(x=325, y=300)

    lamp4 = IntVar()
    lamp4.set(api.get_lamp_kitchen())

    room_4_lamp_on = Radiobutton(root, text="ON", command=lambda: api.change_lamp_kitchen(
        lamp4.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp4, value=1)
    room_4_lamp_on.place(x=320, y=320)

    room_4_lamp_off = Radiobutton(root, text="OFF", command=lambda: api.change_lamp_kitchen(
        lamp4.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp4,  value=0)
    room_4_lamp_off.place(x=320, y=340)

    musik4 = Label(root, text="Musik")
    musik4.place(x=390, y=300)

    mus4 = IntVar()
    mus4.set(api.get_music_kitchen())

    room_4_musik_on = Radiobutton(root, text="ON", command=lambda: api.change_music_kitchen(
        mus4.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus4, value=1)
    room_4_musik_on.place(x=385, y=320)

    room_4_musik_off = Radiobutton(root, text="OFF", command=lambda: api.change_music_kitchen(
        mus4.get(), 1, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus4,  value=0)
    room_4_musik_off.place(x=385, y=340)

    time()

    root.mainloop()
    api.loop_thrd = False


def children():
    api.loop_thrd = True
    root = Tk()
    root.geometry("450x500")
    root.title("My Smart Home")
    login_info = Label(root, text="My Smart Home",
                       font=("Helvatica", 20, "bold"))
    login_info.grid(row=1, column=2, sticky=N)

    def time():
        named_tuple = localtime()  # get struct_time
        time_string = str(
            int(strftime("%S", named_tuple)) % 24)
        lbl.config(text=time_string)
        lbl.after(1000, time)

    lbl = Label(root, font=('times new roman', 20, 'bold'),
                background='white', foreground='black')
    lbl.place(x=200, y=85)

    breakline2 = ttk.Separator(root, orient='horizontal')
    breakline2.grid(row=8, columnspan=100, ipadx=250, pady=10)

    Room_1 = Label(root, text="Bedroom")
    Room_1.place(x=1, y=190)

    AC = Label(root, text="AC", )
    AC.place(x=20, y=210)

    var2 = IntVar()
    var2.set(api.get_ac_bedroom())

    room_1_ac_on = Radiobutton(root, text="ON", command=lambda: api.change_ac_bedroom(
        var2.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var2, value=1)
    room_1_ac_on.place(x=1, y=230)

    room_1_ac_off = Radiobutton(root, text="OFF", command=lambda: api.change_ac_bedroom(
        var2.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var2,  value=0)
    room_1_ac_off.place(x=1, y=250)

    Lampu = Label(root, text='Lampu')
    Lampu.place(x=65, y=210)

    var3 = IntVar()
    var3.set(api.get_lamp_bedroom())

    room_1_lamp_on = Radiobutton(root, text="ON", command=lambda: api.change_lamp_bedroom(
        var3.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var3, value=1)
    room_1_lamp_on.place(x=60, y=230)

    room_1_lamp_off = Radiobutton(root, text="OFF", command=lambda: api.change_lamp_bedroom(
        var3.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var3,  value=0)
    room_1_lamp_off.place(x=60, y=250)

    musik = Label(root, text="Musik")
    musik.place(x=125, y=210)

    var4 = IntVar()
    var4.set(api.get_music_bedroom())

    room_1_musik_on = Radiobutton(root, text="ON", command=lambda: api.change_music_bedroom(
        var4.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var4, value=1)
    room_1_musik_on.place(x=120, y=230)

    room_1_musik_off = Radiobutton(root, text="OFF", command=lambda: api.change_music_bedroom(
        var4.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var4,  value=0)
    room_1_musik_off.place(x=120, y=250)

    Room_2 = Label(root, text="Bathroom")
    Room_2.place(x=1, y=280)

    Lampu2 = Label(root, text='Lampu')
    Lampu2.place(x=10, y=300)

    lamp2 = IntVar()
    lamp2.set(api.get_lamp_bathroom())

    room_2_lamp_on = Radiobutton(root, text="ON", command=lambda: api.change_lamp_bathroom(
        lamp2.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp2, value=1)
    room_2_lamp_on.place(x=1, y=320)

    room_2_lamp_off = Radiobutton(root, text="OFF", command=lambda: api.change_lamp_bathroom(
        lamp2.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp2,  value=0)
    room_2_lamp_off.place(x=1, y=340)

    musik2 = Label(root, text="Musik")
    musik2.place(x=65, y=300)

    mus2 = IntVar()
    mus2.set(api.get_music_bathroom())

    room_2_musik_on = Radiobutton(root, text="ON", command=lambda: api.change_music_bathroom(
        mus2.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus2, value=1)
    room_2_musik_on.place(x=60, y=320)

    room_2_musik_off = Radiobutton(root, text="OFF", command=lambda: api.change_music_bathroom(
        mus2.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus2,  value=0)
    room_2_musik_off.place(x=60, y=340)

    Room_3 = Label(root, text="Living Room")
    Room_3.place(x=270, y=190)

    AC3 = Label(root, text="AC")
    AC3.place(x=280, y=210)

    ac3 = IntVar()
    ac3.set(api.get_ac_living_room())

    room_3_ac_on = Radiobutton(root, text="ON", command=lambda: api.change_ac_living_room(
        ac3.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=ac3, value=1)
    room_3_ac_on.place(x=265, y=230)

    room_3_ac_off = Radiobutton(root, text="OFF", command=lambda: api.change_ac_living_room(
        ac3.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"),  variable=ac3,  value=0)
    room_3_ac_off.place(x=265, y=250)

    Lampu = Label(root, text='Lampu')
    Lampu.place(x=325, y=210)

    lamp3 = IntVar()
    lamp3.set(api.get_lamp_living_room())

    room_3_lamp_on = Radiobutton(root, text="ON", command=lambda: api.change_lamp_living_room(
        lamp3.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp3, value=1)
    room_3_lamp_on.place(x=320, y=230)

    room_3_lamp_off = Radiobutton(root, text="OFF", command=lambda: api.change_lamp_living_room(
        lamp3.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp3,  value=0)
    room_3_lamp_off.place(x=320, y=250)

    musik = Label(root, text="Musik")
    musik.place(x=390, y=210)

    mus3 = IntVar()
    mus3.set(api.get_music_living_room())

    room_3_musik_on = Radiobutton(root, text="ON", command=lambda: api.change_music_living_room(
        mus3.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus3, value=1)
    room_3_musik_on.place(x=385, y=230)

    room_3_musik_off = Radiobutton(root, text="OFF", command=lambda: api.change_music_living_room(
        mus3.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"),  variable=mus3,  value=0)
    room_3_musik_off.place(x=385, y=250)
    Room_4 = Label(root, text="Kitchen")
    Room_4.place(x=270, y=280)

    AC4 = Label(root, text="AC")
    AC4.place(x=280, y=300)

    ac4 = IntVar()
    ac4.set(api.get_ac_kitchen())

    room_4_ac_on = Radiobutton(root, text="ON", command=lambda: api.change_ac_kitchen(
        ac4.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=ac4, value=1)
    room_4_ac_on.place(x=265, y=320)

    room_4_ac_off = Radiobutton(root, text="OFF", command=lambda: api.change_ac_kitchen(
        ac4.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=ac4,  value=0)
    room_4_ac_off.place(x=265, y=340)

    Lampu4 = Label(root, text='Lampu')
    Lampu4.place(x=325, y=300)

    lamp4 = IntVar()
    lamp4.set(api.get_lamp_kitchen())

    room_4_lamp_on = Radiobutton(root, text="ON", command=lambda: api.change_lamp_kitchen(
        lamp4.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp4, value=1)
    room_4_lamp_on.place(x=320, y=320)

    room_4_lamp_off = Radiobutton(root, text="OFF", command=lambda: api.change_lamp_kitchen(
        lamp4.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp4,  value=0)
    room_4_lamp_off.place(x=320, y=340)

    musik4 = Label(root, text="Musik")
    musik4.place(x=390, y=300)

    mus4 = IntVar()
    mus4.set(api.get_music_kitchen())

    room_4_musik_on = Radiobutton(root, text="ON", command=lambda: api.change_music_kitchen(
        mus4.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus4, value=1)
    room_4_musik_on.place(x=385, y=320)

    room_4_musik_off = Radiobutton(root, text="OFF", command=lambda: api.change_music_kitchen(
        mus4.get(), 2, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus4,  value=0)
    room_4_musik_off.place(x=385, y=340)
    time()

    root.mainloop()
    api.loop_thrd = False


def guest():
    api.loop_thrd = True

    root = Tk()
    root.geometry("450x500")
    root.title("My Smart Home")
    login_info = Label(root, text="My Smart Home",
                       font=("Helvatica", 20, "bold"))
    login_info.grid(row=1, column=2, sticky=N)

    guest_lbl = Label(root, text="Guest Mode is ON, You can use Smart Home")
    guest_lbl.place(x=150, y=110)

    auto = Label(root, text="Automatic Mode")
    auto.grid(row=5, column=1, pady=5, sticky=W)

    var1 = IntVar()
    var1.set(api.get_automatic_mode())

    autobtn = Radiobutton(root, text="Automatic", command=lambda: [api.change_automatic_mode(
        4, var1.get(), str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), parent_manu_to_auto(root)], variable=var1, value=1)
    autobtn.grid(row=6, column=1, sticky=W)

    manubtn = Radiobutton(root, text="Manual", command=lambda: api.change_automatic_mode(
        4, var1.get(), str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var1,  value=0)
    manubtn.grid(row=7, column=1, sticky=W)

    def time():
        named_tuple = localtime()  # get struct_time
        time_string = str(
            int(strftime("%S", named_tuple)) % 24)
        lbl.config(text=time_string)
        lbl.after(1000, time)

    lbl = Label(root, font=('times new roman', 20, 'bold'),
                background='white', foreground='black')
    lbl.place(x=200, y=65)

    breakline2 = ttk.Separator(root, orient='horizontal')
    breakline2.grid(row=8, columnspan=100, ipadx=250, pady=10)

    Room_1 = Label(root, text="Bedroom")
    Room_1.place(x=1, y=190)

    AC = Label(root, text="AC", )
    AC.place(x=20, y=210)

    var2 = IntVar()
    var2.set(api.get_ac_bedroom())

    room_1_ac_on = Radiobutton(root, text="ON", command=lambda: api.change_ac_bedroom(
        var2.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var2, value=1)
    room_1_ac_on.place(x=1, y=230)

    room_1_ac_off = Radiobutton(root, text="OFF", command=lambda: api.change_ac_bedroom(
        var2.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var2,  value=0)
    room_1_ac_off.place(x=1, y=250)

    Lampu = Label(root, text='Lampu')
    Lampu.place(x=65, y=210)

    var3 = IntVar()
    var3.set(api.get_lamp_bedroom())

    room_1_lamp_on = Radiobutton(root, text="ON", command=lambda: api.change_lamp_bedroom(
        var3.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var3, value=1)
    room_1_lamp_on.place(x=60, y=230)

    room_1_lamp_off = Radiobutton(root, text="OFF", command=lambda: api.change_lamp_bedroom(
        var3.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var3,  value=0)
    room_1_lamp_off.place(x=60, y=250)

    musik = Label(root, text="Musik")
    musik.place(x=125, y=210)

    var4 = IntVar()
    var4.set(api.get_music_bedroom())

    room_1_musik_on = Radiobutton(root, text="ON", command=lambda: api.change_music_bedroom(
        var4.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var4, value=1)
    room_1_musik_on.place(x=120, y=230)

    room_1_musik_off = Radiobutton(root, text="OFF", command=lambda: api.change_music_bedroom(
        var4.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=var4,  value=0)
    room_1_musik_off.place(x=120, y=250)

    Room_2 = Label(root, text="Bathroom")
    Room_2.place(x=1, y=280)

    Lampu2 = Label(root, text='Lampu')
    Lampu2.place(x=10, y=300)

    lamp2 = IntVar()
    lamp2.set(api.get_lamp_bathroom())

    room_2_lamp_on = Radiobutton(root, text="ON", command=lambda: api.change_lamp_bathroom(
        lamp2.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp2, value=1)
    room_2_lamp_on.place(x=1, y=320)

    room_2_lamp_off = Radiobutton(root, text="OFF", command=lambda: api.change_lamp_bathroom(
        lamp2.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp2,  value=0)
    room_2_lamp_off.place(x=1, y=340)

    musik2 = Label(root, text="Musik")
    musik2.place(x=65, y=300)

    mus2 = IntVar()
    mus2.set(api.get_music_bathroom())

    room_2_musik_on = Radiobutton(root, text="ON", command=lambda: api.change_music_bathroom(
        mus2.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus2, value=1)
    room_2_musik_on.place(x=60, y=320)

    room_2_musik_off = Radiobutton(root, text="OFF", command=lambda: api.change_music_bathroom(
        mus2.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus2,  value=0)
    room_2_musik_off.place(x=60, y=340)

    Room_3 = Label(root, text="Living Room")
    Room_3.place(x=270, y=190)

    AC3 = Label(root, text="AC")
    AC3.place(x=280, y=210)

    ac3 = IntVar()
    ac3.set(api.get_ac_living_room())

    room_3_ac_on = Radiobutton(root, text="ON", command=lambda: api.change_ac_living_room(
        ac3.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=ac3, value=1)
    room_3_ac_on.place(x=265, y=230)

    room_3_ac_off = Radiobutton(root, text="OFF", command=lambda: api.change_ac_living_room(
        ac3.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"),  variable=ac3,  value=0)
    room_3_ac_off.place(x=265, y=250)

    Lampu = Label(root, text='Lampu')
    Lampu.place(x=325, y=210)

    lamp3 = IntVar()
    lamp3.set(api.get_lamp_living_room())

    room_3_lamp_on = Radiobutton(root, text="ON", command=lambda: api.change_lamp_living_room(
        lamp3.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp3, value=1)
    room_3_lamp_on.place(x=320, y=230)

    room_3_lamp_off = Radiobutton(root, text="OFF", command=lambda: api.change_lamp_living_room(
        lamp3.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp3,  value=0)
    room_3_lamp_off.place(x=320, y=250)

    musik = Label(root, text="Musik")
    musik.place(x=390, y=210)

    mus3 = IntVar()
    mus3.set(api.get_music_living_room())

    room_3_musik_on = Radiobutton(root, text="ON", command=lambda: api.change_music_living_room(
        mus3.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus3, value=1)
    room_3_musik_on.place(x=385, y=230)

    room_3_musik_off = Radiobutton(root, text="OFF", command=lambda: api.change_music_living_room(
        mus3.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"),  variable=mus3,  value=0)
    room_3_musik_off.place(x=385, y=250)
    Room_4 = Label(root, text="Kitchen")
    Room_4.place(x=270, y=280)

    AC4 = Label(root, text="AC")
    AC4.place(x=280, y=300)

    ac4 = IntVar()
    ac4.set(api.get_ac_kitchen())

    room_4_ac_on = Radiobutton(root, text="ON", command=lambda: api.change_ac_kitchen(
        ac4.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=ac4, value=1)
    room_4_ac_on.place(x=265, y=320)

    room_4_ac_off = Radiobutton(root, text="OFF", command=lambda: api.change_ac_kitchen(
        ac4.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=ac4,  value=0)
    room_4_ac_off.place(x=265, y=340)

    Lampu4 = Label(root, text='Lampu')
    Lampu4.place(x=325, y=300)

    lamp4 = IntVar()
    lamp4.set(api.get_lamp_kitchen())

    room_4_lamp_on = Radiobutton(root, text="ON", command=lambda: api.change_lamp_kitchen(
        lamp4.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp4, value=1)
    room_4_lamp_on.place(x=320, y=320)

    room_4_lamp_off = Radiobutton(root, text="OFF", command=lambda: api.change_lamp_kitchen(
        lamp4.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=lamp4,  value=0)
    room_4_lamp_off.place(x=320, y=340)

    musik4 = Label(root, text="Musik")
    musik4.place(x=390, y=300)

    mus4 = IntVar()
    mus4.set(api.get_music_kitchen())

    room_4_musik_on = Radiobutton(root, text="ON", command=lambda: api.change_music_kitchen(
        mus4.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus4, value=1)
    room_4_musik_on.place(x=385, y=320)

    room_4_musik_off = Radiobutton(root, text="OFF", command=lambda: api.change_music_kitchen(
        mus4.get(), 4, str(int(strftime("%S", localtime())) % 24).zfill(2) + ":00:00"), variable=mus4,  value=0)
    room_4_musik_off.place(x=385, y=340)

    time()

    root.mainloop()
    api.loop_thrd = False


def admin():
    root = Tk()
    root.geometry("450x300")
    root.title("My Smart Home")
    login_info = Label(root, text="My Smart Home",
                       font=("Helvatica", 20, "bold"))
    login_info.grid(row=1, column=2, sticky=N)

    admin = Label(root, text="ADMIN MODE", font=(
        "Times New Roman", 13, "bold"))
    admin.place(x=300, y=270)

    usrn = StringVar()
    psw = StringVar()

    username = Label(root, text="username")
    username.grid(row=2, column=1, pady=10, sticky=W)
    usern = Entry(root, textvariable=usrn, width=30)
    usern.grid(row=2, column=2, sticky=W)

    password = Label(root, text="password")
    password.grid(row=3, column=1, pady=5, sticky=W)
    passw = Entry(root, textvariable=psw, width=30)
    passw.grid(row=3, column=2, sticky=W)

    update = Button(root, command=lambda: api.change_pass(
        usrn.get(), psw.get()), text="Update")
    update.grid(row=4, column=2, pady=5, sticky=N)

    def time():
        named_tuple = localtime()  # get struct_time
        time_string = str(
            int(strftime("%S", named_tuple)) % 24)
        lbl.config(text=time_string)
        lbl.after(1000, time)

    lbl = Label(root, font=('times new roman', 20, 'bold'),
                background='white', foreground='black')
    lbl.grid(row=5, column=2, pady=5, sticky=N)

    time()
    root.mainloop()


def time():
    string = strftime('%S', localtime())
    string = str(int(string) % 24)
    return string


def parent_manu_to_auto(root):
    # root.quit()
    root.destroy()
    parent_auto()


def parent_auto_to_manu(root):
    root.destroy()
    parent()


def guest_auto():
    children_auto()


'''
tes = Login()
tes.login()'''
