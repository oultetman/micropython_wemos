from machine import Pin, ADC
import machine

pins = {"d0": 3, "d1": 1, "d2": 16, "d3": 5, "d4": 4, "d5": 0, "d6": 2, "d7": 14, "d8": 12, "d9": 13, "d10": 15,
            "d11": 13, "d12": 12, "d13": 14, "d14": 4, "d15": 5, 0: 3, 1: 1, 2: 16, 3: 5, 4: 4, 5: 0, 6: 2, 7: 14,
            8: 12, 9: 13, 10: 15, 11: 13, 12: 12, 13: 14, 14: 4, 15: 5}

def PinWemos(pin_name, mode=-1, pull_up=-1, **kwargs):
    pin = pins.get(pin_name)
    p = Pin(pin, mode, pull_up)
    if kwargs.get("value") is not None:
        p.value(kwargs.get("value"))
    return p


def AdcA082():
    return ADC(0)


def I2C():
    return machine.I2C(scl=Pin(5), sda=Pin(4))


def PWM(pin_name, freq=5, duty=512):
    pin = pins.get(pin_name)
    if pin==16:
        raise ValueError("pin value prohibited")
    return machine.PWM(Pin(pin), freq=freq, duty=duty)

