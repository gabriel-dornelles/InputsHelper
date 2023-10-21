from .constant import MAX, MIN
from .deadzone import analog

class Analog:
    def __init__(self, name, joystick):
        self.__name = name
        self.__joystick = joystick
    
    @property
    def active(self):
        return bool(
            # left stick
            self.__name == "LS_UP"    and round(self.__joystick.axisValues[1] * MAX) < analog["Left"][0] or
            self.__name == "LS_DOWN"  and round(self.__joystick.axisValues[1] * MAX) > analog["Left"][1] or
            self.__name == "LS_LEFT"  and round(self.__joystick.axisValues[0] * MAX) < analog["Left"][2] or
            self.__name == "LS_RIGHT" and round(self.__joystick.axisValues[0] * MAX) > analog["Left"][3] or
            
            # right stick
            self.__name == "RS_UP"    and round(self.__joystick.axisValues[1] * MAX) < analog["Right"][0] or
            self.__name == "RS_DOWN"  and round(self.__joystick.axisValues[1] * MAX) > analog["Right"][1] or
            self.__name == "RS_LEFT"  and round(self.__joystick.axisValues[0] * MAX) < analog["Right"][2] or
            self.__name == "RS_RIGHT" and round(self.__joystick.axisValues[0] * MAX) > analog["Right"][3]
        )
        