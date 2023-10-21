from .constant import MAX, MIN
from .deadzone import trigger
from .variable import activeButtons

class Trigger:
    def __init__(self, name, joystick):
        self.__name     = name
        self.__joystick = joystick
    
    @property
    def hold(self):
        return bool(
            self.__name == "LT" and round(self.__joystick.axisValues[4] * MAX) > trigger["Left"] or
            self.__name == "RT" and round(self.__joystick.axisValues[5] * MAX) > trigger["Right"]
        )
    
    @property
    def pressed(self):
        if not self.__name in activeButtons:
            if self.__name == "LT" and round(self.__joystick.axisValues[4] * MAX) > trigger["Left"] or self.__name == "RT" and round(self.__joystick.axisValues[5] * MAX) > trigger["Right"]:
                activeButtons.append(self.__name)
                return True
        else:
            if self.__name == "LT" and round(self.__joystick.axisValues[4] * MAX) < trigger["Left"] or self.__name == "RT" and round(self.__joystick.axisValues[5] * MAX) < trigger["Right"]:
                activeButtons.remove(self.__name)
