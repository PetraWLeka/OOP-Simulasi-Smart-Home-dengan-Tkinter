import random


def all_suhu():
    suhu_bedroom = round(random.uniform(20.5, 40.9), 2)
    suhu_kitchen = round(random.uniform(20.5, 40.9), 2)
    suhu_living_room = round(random.uniform(20.5, 40.9), 2)
    all_suhu = [suhu_bedroom, suhu_kitchen, suhu_living_room]
    return all_suhu


def all_orang():
    orang_bedroom = random.randint(0, 10)
    orang_kitchen = random.randint(0, 10)
    orang_bathroom = random.randint(0, 10)
    orang_living_room = random.randint(0, 10)
    all_orang = [orang_bedroom, orang_kitchen,
                 orang_bathroom, orang_living_room]
    return all_orang


def all_cahaya():
    cahaya_bedroom = random.randint(10, 500)
    cahaya_kitchen = random.randint(10, 500)
    cahaya_bathroom = random.randint(10, 500)
    cahaya_living_room = random.randint(10, 500)
    all_cahaya = [cahaya_bedroom, cahaya_kitchen,
                  cahaya_bathroom, cahaya_living_room]
    return all_cahaya
