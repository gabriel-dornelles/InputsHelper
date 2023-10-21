from .variable import activeButtons

class Button:
    def __init__(self, button, joystick):
        self.__button   = button
        self.__joystick = joystick
    
    @property
    def hold(self):
        return bool(self.__button in self.__joystick.activeButtons)
    
    @property
    def pressed(self):
        if not self.__button in activeButtons:
            if self.__button in self.__joystick.activeButtons:
                activeButtons.append(self.__button)
                return True
        else:
            if not self.__button in self.__joystick.activeButtons:
                activeButtons.remove(self.__button)
    