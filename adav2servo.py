class Servo:
    """ A servo motor connected to one of the 4 remaining PWM output of the shield.
        Works best if the frequency of the PCA9685 is about 50Hz.
    """

    def __init__(self, pca, pwm, min_us=500, max_us=2500, range=180):
        """ Initialize a servo motor driven by PWM number 'pwm'.
            'pwm' should be 0, 1, 14 or 15.
            'min_us' and 'max_us' are the min and max duty duration in microseconds
            to get the min and max rotation positions.
            'range is the rotation range in degrees.
        """
        if not pwm in (0, 1, 14, 15):
            raise ValueError('Servos can be driven only on ports 0, 1, 14 and 15.')
        self._pca = pca
        self._pwm = pwm
        self._minus = min_us
        self._maxus = max_us
        self._range = range
        pca.setDuty(self._pwm, 0)  # release the servo
        self._period = 1e6 / pca.getFreq()
        self._minduty = int(self._minus / (self._period / 4096))
        self._maxduty = int(self._maxus / (self._period / 4096))

    def setDutyTime(self, us):
        """ Set the duty time of the servo in microseconds. """
        self._pca.setDuty(self._pwm, int(us / (self._period / 4096)))

    def release(self):
        """ Release the servo (set PWM to 0). """
        self._pca.setDuty(self._pwm, 0)

    def position(self, degrees):
        """ Set the position of the servo in degrees. """
        self._pca.setDuty(self._pwm, int(self._minduty + (self._maxduty - self._minduty) * (degrees / self._range)))