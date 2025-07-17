import machine
import utime

class BtAudioAmp:
    """
    Bluetooth Audio Amplifier Control
    """
    SHOT_HOLD = 100
    LONG_HOLD = 1300
    
    def __init__(self, mode, scan, down, up, shot_hold_ms=SHOT_HOLD, long_hold_ms=LONG_HOLD):
        """
        Initialize the Bluetooth Audio Amplifier control pins.
        :param mode: pin number for mode control
        :param scan: pin number for scan control
        :param down: pin number for down/previous control
        :param upn: pin number for up/next control
        """        
        self._mode = machine.Pin(mode, mode=machine.Pin.OUT, value=0)
        self._scan = machine.Pin(scan, mode=machine.Pin.OUT, value=0)
        self._down_prev = machine.Pin(down, mode=machine.Pin.OUT, value=0)
        self._up_next = machine.Pin(up, mode=machine.Pin.OUT, value=0)
        self._shot_hold_ms = shot_hold_ms
        self._long_hold_ms = long_hold_ms
        
    def __press(self, pin, hold_ms):
        """
        Press a button for a specified duration.
        :param pin: Pin to press
        :param hold_ms: Duration to press the button in milliseconds
        """
        pin.value(1)
        utime.sleep_ms(hold_ms)
        pin.value(0)
        utime.sleep_us(80)

    def down(self):
        """
        Press the down/previous button for a specified duration.
        """
        self.__press(self._down_prev, self._long_hold_ms)

    def up(self):
        """
        Press the up/next button for a specified duration.
        """
        self.__press(self._up_next, self._long_hold_ms)

    def prev(self):   
        """
        Press the down/previous button for a specified duration.
        """
        self.__press(self._down_prev, self._shot_hold_ms)        

    def next(self):
        """
        Press the up/next button for a specified duration.
        """
        self.__press(self._up_next, self._shot_hold_ms)

    def pause_resume(self):
        """
        Press the mode button for a specified duration.
        :param duration: Duration to press the button in milliseconds
        """
        self.__press(self._scan, self._shot_hold_ms)
