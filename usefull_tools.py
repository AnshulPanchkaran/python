import random
feet_in_mile = 5280
meters_in_kilometer =1000
battels = ["john lennom","paul mc cartney","george harrison","ringo star"]


def get_file_ext(filename):
    return filename[filename.index(" . ") + 1:]

def rool_dice(num):
    return random.randint(1,num)