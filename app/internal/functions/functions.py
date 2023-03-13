from pytz import timezone 
from datetime import datetime
from .weather import getWeather

def getTime():
    ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('දැන් වෙලාව %H:%M')
    print(ind_time)
    return ind_time




get_func = {
    'time': getTime,
    'weather': getWeather
    }

















