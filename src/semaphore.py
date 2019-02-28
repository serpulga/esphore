from machine import Pin


class Semaphore(object):

    RED_PIN = 2
    GREEN_PIN = 4
    CROSS_DETECTION_PIN = 12
    CROSS_INDICATOR_PIN = 16

    def __init__(self, period=30, cross_time=10):
        self.period = period
        self.cross_time = cross_time
        self.crossing = False

        self.init_pins()

        self.red_on()

    def init_pins(self):
        cls = self.__class__

        def cross_handler(pin):
            self.cross_request()

        self._red_pin = Pin(cls.RED_PIN, Pin.OUT)
        self._green_pin = Pin(cls.GREEN_PIN, Pin.OUT)
        self._cross_indicator_pin = Pin(cls.CROSS_INDICATOR_PIN, Pin.OUT)
        self._cross_pin = Pin(cls.CROSS_DETECTION_PIN, Pin.IN)
        self._cross_pin.irq(trigger=Pin.IRQ_FALLING, handler=cross_handler)

        self._cross_indicator_pin.on()

    def red_on(self):
        self.is_red = True
        self.is_green = False

        self._red_pin.on()
        self._green_pin.off()

    def green_on(self):
        self.is_red = False
        self.is_green = True

        self._red_pin.off()
        self._green_pin.on()

    def cross_request(self):
        self.crossing = True
        self._cross_indicator_pin.off()

    def cross_request_completed(self):
        self.crossing = False
        self._cross_indicator_pin.on()
