from machine import Pin, PWM
pins = {"d0": 3, "d1": 1, "d2": 16, "d3": 5, "d4": 4, "d5": 0, "d6": 2, "d7": 14, "d8": 12, "d9": 13, "d10": 15,
        "d11": 13, "d12": 12, "d13": 14, "d14": 4, "d15": 5, 0: 3, 1: 1, 2: 16, 3: 5, 4: 4, 5: 0, 6: 2, 7: 14,
        8: 12, 9: 13, 10: 15, 11: 13, 12: 12, 13: 14, 14: 4, 15: 5}

class Servo:
    # these defaults work for the standard TowerPro SG90
    __servo_pwm_freq = 50
    __min_u10_duty = 26 - 0 # offset for correction
    __max_u10_duty = 123 - 0  # offset for correction
    min_angle = 0
    max_angle = 180
    current_angle = 0.001


    def __init__(self, pin):
        self.__initialise(pin)


    def update_settings(self, servo_pwm_freq, min_u10_duty, max_u10_duty, min_angle, max_angle, pin):
        self.__servo_pwm_freq = servo_pwm_freq
        self.__min_u10_duty = min_u10_duty
        self.__max_u10_duty = max_u10_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.__initialise(pin)


    def move(self, angle):
        # round to 2 decimal places, so we have a chance of reducing unwanted servo adjustments
        angle = round(angle, 2)
        # do we need to move?
        if angle == self.current_angle:
            return
        self.current_angle = angle
        # calculate the new duty cycle and move the motor
        duty_u10 = self.__angle_to_u10_duty(angle)
        self.__motor.duty(duty_u10)

    def __angle_to_u10_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u10_duty


    def __initialise(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (self.__max_u10_duty - self.__min_u10_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(pin)
        self.__motor.freq(self.__servo_pwm_freq)