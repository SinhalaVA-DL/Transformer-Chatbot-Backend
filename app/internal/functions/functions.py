from pytz import timezone
from datetime import datetime
from .weather import getWeather


def getTime():
    ind_time = datetime.now(timezone("Asia/Kolkata"))
    datetime_object = datetime.fromisoformat(str(ind_time))
    date = datetime_object.date()
    time = datetime_object.time().strftime("%H:%M:%S")
    return "දැන් වෙලාව" + " " + str(time)


get_func = {
    'time': getTime,
    'weather': getWeather
}
