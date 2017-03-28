import mraa
import time
from th02 import *
from servo import *
"""
PIN Number
"""

MOISTURE_PIN = 1
LIGHT_PIN = 2
RELAY_PIN = 5

"""
Set Pin
"""
try:
    moisture_signal = mraa.Aio(MOISTURE_PIN)
    light_signal = mraa.Aio(LIGHT_PIN)
    relay_signal = mraa.Gpio(RELAY_PIN)
    relay_signal.dir(mraa.DIR_OUT)
except Exception as e:
    print ('Error: {}'.format(e))

th02 = TH02()


def get_moisture():
    """
    Return moisture value
    :param analog_num:
    :return:
    """
    try:
        moisture = moisture_signal.read()
        print ('moisture: {}\n'.format(moisture))
        return moisture

    except Exception as e:
        print ("Are you sure you have an ADC?")

    return False


def get_light():
    """
    Return Light value
    :param analog_num:
    :return:
    """

    try:
        light = light_signal.readFloat()
        # print "%.5f" % x.readFloat()
        print ('light: {}\n'.format(light))
        return light
    except Exception as e:
        print ("Are you sure you have an ADC?")

    return False


def set_relay(flag=0):
    """
    Return Relay status
    :param digital_pin:
    :return:
    """
    try:
        if flag == 0:
            relay_signal.write(0)
        elif flag == 1:
            relay_signal.write(1)
        else:
            print ('set flag either of 0 or 1')
    except Exception as e:
        print ('Error: {}'.format(e))


def get_temp_hum():
    """
    Return temp and humidity
    :param i2c_pin:
    :return:
    """
    temp = th02.getTemperature()
    humidity = th02.getHumidity()
    print ('tem: {}\n'.format(temp))
    print ('humidity: {}\n'.format(humidity))
    return temp, humidity


def set_servo():
    """
    Return servo status
    :return:
    """

if __name__ == '__main__':
    while 1:
        get_moisture()
        get_light()
        get_temp_hum()
        time.sleep(5)
