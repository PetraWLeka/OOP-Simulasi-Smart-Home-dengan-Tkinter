from time import strftime
from time import localtime
print("2".zfill(2))
print(str(int(strftime("%S", localtime())) % 24).zfill(2))
