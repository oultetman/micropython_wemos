from machine import Pin
import machine


pins = {"d0": 3, "d1": 1, "d2": 26, "d3": 25, "d4": 17, "d5": 16, "d6": 27, "d7": 14, "d8": 12, "d9": 13, "d10": 5,
        "d11": 23, "d12": 19, "d13": 18, "sda": 21, "scl": 22, 0: 3, 1: 1, 2: 26, 3: 25, 4: 17, 5: 16, 6: 27, 7: 14,
        8: 12, 9: 13, 10: 5, 11: 23, 12: 19, 13: 18,"a0": 2, "a1": 4, "a2": 36, "a3": 34, "a4": 38, "a5": 39}

def PinWemos(pin_name, mode=-1, pull_up=-1, **kwargs):
    pin = pins.get(pin_name)
    p = Pin(pin, mode, pull_up)
    if kwargs.get("value") is not None:
        p.value(kwargs.get("value"))
    return p

def ADC(pin_name):
    pins = {"a0": 2, "a1": 4, "a2": 36, "a3": 34, "a4": 38, "a5": 39, 0: 2, 1: 4, 2: 36, 3: 34, 4: 38, 5: 39}
    pin_value = pins.get(pin_name)
    return machine.ADC(Pin(pin_value))

def I2C():
    return machine.SoftI2C(scl=Pin(22), sda=Pin(21))