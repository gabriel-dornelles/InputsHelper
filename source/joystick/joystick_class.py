from bge.logic      import joysticks
from .constant      import MAX, MIN
from .deadzone      import analog, trigger
from .analog_class  import Analog
from .trigger_class import Trigger
from .button_class  import Button

class Joystick:
    def __init__(self, index):
        self.__joystick = joysticks[index]
        
        self.keys = {
            # d-pad
            "DPAD_UP"    : Button(11, self.__joystick),
            "DPAD_DOWN"  : Button(12, self.__joystick),
            "DPAD_LEFT"  : Button(13, self.__joystick),
            "DPAD_RIGHT" : Button(14, self.__joystick),
                
            # left stick
            "LS_UP"    : Analog("LS_UP",    self.__joystick),
            "LS_DOWN"  : Analog("LS_DOWN",  self.__joystick),
            "LS_LEFT"  : Analog("LS_LEFT",  self.__joystick),
            "LS_RIGHT" : Analog("LS_RIGHT", self.__joystick),
            "LS_BUTTON" : Button(7, self.__joystick),
            
            # right stick
            "RS_UP"    : Analog("RS_UP",    self.__joystick),
            "RS_DOWN"  : Analog("RS_DOWN",  self.__joystick),
            "RS_LEFT"  : Analog("RS_LEFT",  self.__joystick),
            "RS_RIGHT" : Analog("RS_RIGHT", self.__joystick),
            "RS_BUTTON" : Button(8, self.__joystick),
            
            # triggers
            "LT" : Trigger("LT", self.__joystick),
            "RT" : Trigger("RT", self.__joystick),
            
            # bumpers
            "LB" : Button(9, self.__joystick),
            "RB" : Button(10, self.__joystick),
            
            # functions
            "START"  : Button(4, self.__joystick),
            "SELECT" : Button(6, self.__joystick),
            
            # actions
            "A" : Button(0, self.__joystick),
            "B" : Button(1, self.__joystick),
            "X" : Button(2, self.__joystick),
            "Y" : Button(3, self.__joystick),
    }
    
    def __getitem__(self, key):
        if hasattr(self, "keys"):
            try:
                return self.keys[key]
            except:
                raise Exception(
                    f'~Key Accessing~ >> An error occurred when trying to access the given key, check if the key exists and try again'
                )
        else:
            raise Exception(
                f'~Key Accessing~ >> Joystick keys was not initialized correctly'
            )
    
    def setDeadzone(self, target, value):
        if type(target) != str or type(value) != int or value > MAX or value < -MAX:
            raise Exception(
                f"~setDeadzone~ >> Invalid parameters"
            )
        else:
            # left stick
            if   target == "LS_UP"    and value > -MAX: analog["Left"][0] = value
            elif target == "LS_DOWN"  and value <  MAX: analog["Left"][1] = value
            elif target == "LS_LEFT"  and value > -MAX: analog["Left"][2] = value
            elif target == "LS_RIGHT" and value <  MAX: analog["Left"][3] = value
            
            # right stick
            elif target == "RS_UP"    and value > -MAX: analog["Right"][0] = value
            elif target == "RS_DOWN"  and value <  MAX: analog["Right"][1] = value
            elif target == "RS_LEFT"  and value > -MAX: analog["Right"][2] = value
            elif target == "RS_RIGHT" and value <  MAX: analog["Right"][3] = value
            
            # triggers
            elif target == "LT" and value < MAX: trigger["Left"]  = value
            elif target == "RT" and value < MAX: trigger["Right"] = value
            
    def vibrate(self, duration, strength):
        self.__joystick.duration = duration if type(duration) == int else 0
        
        if type(strength) != tuple or type(strength[0]) != float or type(strength[1]) != float:
            raise Exception(
                f'~vibrate function~ >> Invalid strength values'
            )
        else:
            self.__joystick.strengthLeft  = strength[0]
            self.__joystick.strengthRight = strength[1]
        
        self.__joystick.startVibration()
    
    def stopVibration(self):
        if self.isVibrating():
            self.__joystick.stopVibration()
    
    def isVibrating(self):
        return self.__joystick.isVibrating
    