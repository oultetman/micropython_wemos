class DCMotor:
    """ A DC motor connected to two of the side connectors
        labelled M1, M2, M3 and M4 on the shield.
    """
    # Channels of the PCA9685 that are driving the motor ports M1, M2, M3 and M4
    _MOTORS = (
        {'pwm': 8, 'in1': 10, 'in2': 9},  # Motor 1
        {'pwm': 13, 'in1': 11, 'in2': 12},  # Motor 2
        {'pwm': 2, 'in1': 4, 'in2': 3},  # Motor 3
        {'pwm': 7, 'in1': 5, 'in2': 6}  # Motor 4
    )

    def __init__(self, pca, motor):
        """ Initialize a DC motor driven by PCA9685 'pca' on port 'motor' """
        self._pca = pca
        if (motor < 1) or (motor > 4):
            raise ValueError('Invalid motor number (1-4)')
        self._pwm = DCMotor._MOTORS[motor - 1]['pwm']
        self._in1 = DCMotor._MOTORS[motor - 1]['in1']
        self._in2 = DCMotor._MOTORS[motor - 1]['in2']

    def throttle(self, th):  # th is -4096..4096
        """ Set the throttle of this motor to 'th'.
            Negative values of 'th' make the motor run in the reverse direction
            compared to positive values. The absolute value of 'th' varies from:
              0: the motor is stopped, to
              4096: the motor is at max speed.
        """
        if th > 0:  # Forward
            self._pca.setDuty(self._in2, 0)
            self._pca.setDuty(self._in1, 4096)
        elif th == 0:
            self._pca.setDuty(self._in2, 0)
            self._pca.setDuty(self._in1, 0)
        else:
            self._pca.setDuty(self._in1, 0)
            self._pca.setDuty(self._in2, 4096)
            th = -th
        self._pca.setDuty(self._pwm, th)

    def brake(self):
        """ Make the motor stop by setting the PWM to 0 while maintaining the voltage.
            This stops the motor more quickly than juste setting the throttle to 0.
        """
        self._pca.setDuty(self._in1, 4096)
        self._pca.setDuty(self._in2, 4096)
        self._pca.setDuty(self._pwm, 0)