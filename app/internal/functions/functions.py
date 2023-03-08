import datetime


def getTime():
    return datetime.datetime.now().strftime("%H:%M:%S")


def getWeather():
    return "sunny"


get_func = {
    'time': getTime,
    'weather': getWeather
    }

















