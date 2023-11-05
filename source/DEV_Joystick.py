# bge module
import bge

# constants
DEFAULT_DEADZONE = 5000
DEADZONE_MIN     = 0
DEADZONE_MAX     = 65536

class Analog:
    
    def __init__(self, analog_name, joystick, deadzones):
        
        # get analog name and joystick
        self.__name      = analog_name
        self.__joystick  = joystick
        self.__deadzones = deadzones
    
    @property
    def active(self):
        
        return bool(
            
            # left analog
            self.__name == "LA_UP"    and round(self.__joystick.axisValues[1] * DEADZONE_MAX) < self.__deadzones["analogs"][self.__name] or
            self.__name == "LA_DOWN"  and round(self.__joystick.axisValues[1] * DEADZONE_MAX) > self.__deadzones["analogs"][self.__name] or
            self.__name == "LA_LEFT"  and round(self.__joystick.axisValues[0] * DEADZONE_MAX) < self.__deadzones["analogs"][self.__name] or
            self.__name == "LA_RIGHT" and round(self.__joystick.axisValues[0] * DEADZONE_MAX) > self.__deadzones["analogs"][self.__name] or
            
            # right analog
            self.__name == "RA_UP"    and round(self.__joystick.axisValues[3] * DEADZONE_MAX) < self.__deadzones["analogs"][self.__name] or
            self.__name == "RA_DOWN"  and round(self.__joystick.axisValues[3] * DEADZONE_MAX) > self.__deadzones["analogs"][self.__name] or
            self.__name == "RA_LEFT"  and round(self.__joystick.axisValues[2] * DEADZONE_MAX) < self.__deadzones["analogs"][self.__name] or
            self.__name == "RA_RIGHT" and round(self.__joystick.axisValues[2] * DEADZONE_MAX) > self.__deadzones["analogs"][self.__name]
            
        )
        
class Trigger:
    
    def __init__(self, trigger_name, joystick, deadzones):

        # get trigger
        self.__trigger_name   = trigger_name
        self.__trigger_number = 4 if self.__trigger_name == "LT" else 5
        
        # get joystick
        self.__joystick = joystick
        
        # get deadzones
        self.__deadzones = deadzones
        
        # a list containing the active triggers
        self.__activeTriggers = []
    
    @property
    def hold(self):
        
        return round(self.__joystick.axisValues[self.__trigger_number] * DEADZONE_MAX) > self.__deadzones["triggers"][self.__trigger_name]
    
    @property
    def pressed(self):
        
        if not self.__trigger_name in self.__activeTriggers and self.hold:
            
            self.__activeTriggers.append(self.__trigger_name)
            return True
        
        elif not self.hold and self.__trigger_name in self.__activeTriggers:
            
            self.__activeTriggers.remove(self.__trigger_name)
            
class Button:
    
    def __init__(self, button_number, joystick):
        
        # get joystick and button number
        self.__button   = button_number
        self.__joystick = joystick
        
        # a list containing the active buttons
        self.__activeButtons = []
    
    @property
    def hold(self):
        
        return self.__button in self.__joystick.activeButtons
    
    @property
    def pressed(self):

        if not self.__button in self.__activeButtons and self.__button in self.__joystick.activeButtons:
            
            self.__activeButtons.append(self.__button)
            return True
        
        else:
            
            if not self.__button in self.__joystick.activeButtons and self.__button in self.__activeButtons:
                
                self.__activeButtons.remove(self.__button)
                
class Joystick:
    
    def __init__(self, controller_index):

        if type(controller_index) != int:
            
            raise Exception(
                "Parameter should be an integer"
            )
        
        elif controller_index < 0 or controller_index > 7:
            
            raise Exception(   
                "Index controller should be between 0 and 7"
            )
        
        elif bge.logic.joysticks[controller_index] is None:
            
            raise Exception(
                
                "Game Controller not found in the given index"
                
            )
        
        else:
            
            # get joystick
            self.__joystick = bge.logic.joysticks[controller_index]
            
            # initialize deadzones
            self.__deadzones = {
    
                "analogs" : {
                    
                    # left
                    "LA_UP"    : -DEFAULT_DEADZONE,
                    "LA_DOWN"  :  DEFAULT_DEADZONE,
                    "LA_LEFT"  : -DEFAULT_DEADZONE,
                    "LA_RIGHT" :  DEFAULT_DEADZONE,
                    
                    # right
                    "RA_UP"    : -DEFAULT_DEADZONE,
                    "RA_DOWN"  :  DEFAULT_DEADZONE,
                    "RA_LEFT"  : -DEFAULT_DEADZONE,
                    "RA_RIGHT" :  DEFAULT_DEADZONE
                    
                },
                
                "triggers" : {
                    
                    "LT" : DEFAULT_DEADZONE,
                    "RT" : DEFAULT_DEADZONE
                    
                }
                
            }
            
            # initialize keys
            self.keys = {
                
                # dpad
                "DPAD_UP"    : Button(11, self.__joystick),
                "DPAD_DOWN"  : Button(12, self.__joystick),
                "DPAD_LEFT"  : Button(13, self.__joystick),
                "DPAD_RIGHT" : Button(14, self.__joystick),
                
                # left analog
                "LA_UP"     : Analog("LA_UP",    self.__joystick, self.__deadzones),
                "LA_DOWN"   : Analog("LA_DOWN",  self.__joystick, self.__deadzones),
                "LA_LEFT"   : Analog("LA_LEFT",  self.__joystick, self.__deadzones),
                "LA_RIGHT"  : Analog("LA_RIGHT", self.__joystick, self.__deadzones),
                "LA_BUTTON" : Button(7, self.__joystick),
                
                # right analog
                "RA_UP"     : Analog("RA_UP",    self.__joystick, self.__deadzones),
                "RA_DOWN"   : Analog("RA_DOWN",  self.__joystick, self.__deadzones),
                "RA_LEFT"   : Analog("RA_LEFT",  self.__joystick, self.__deadzones),
                "RA_RIGHT"  : Analog("RA_RIGHT", self.__joystick, self.__deadzones),
                "RA_BUTTON" : Button(8, self.__joystick),
                
                # triggers
                "LT" : Trigger("LT", self.__joystick, self.__deadzones),
                "RT" : Trigger("RT", self.__joystick, self.__deadzones),
                
                # bumpers
                "LB" : Button(9,  self.__joystick),
                "RB" : Button(10, self.__joystick),
                
                # function buttons
                "START"  : Button(6, self.__joystick),
                "SELECT" : Button(4, self.__joystick),
                
                # action buttons
                "A" : Button(0, self.__joystick),
                "B" : Button(1, self.__joystick),
                "X" : Button(2, self.__joystick),
                "Y" : Button(3, self.__joystick)
                
            }

    def __getitem__(self, key):
        
        if hasattr(self, "keys"):
            
            try:
                
                return self.keys[key]
            
            except:
                
                raise Exception(
                    "Couldn't access the given key"
                )
        
        else:
            
            raise Exception(
                "Joystick keys was not initialized"
            )
    
    def setDeadzone(self, target, value):
        
        if type(target) != str:
            
            raise Exception(
                
                "Target should be string"
                
            )
        
        elif value > DEADZONE_MAX or value < -DEADZONE_MAX:
            
            raise Exception(
                
                f"Value should be between {-DEADZONE_MAX} to {DEADZONE_MAX}"
                
            )
        
        else:
            
            if target in self.__deadzones["analogs"]:
                
                if target in ["LA_UP", "LA_LEFT", "RA_UP", "RA_LEFT"] and value > 0:
                    
                    raise Exception(
                        
                        f"This target only receives negative values from -0 to {-DEADZONE_MAX}"
                        
                    )
                
                elif target in ["LA_RIGHT", "LA_DOWN", "RA_RIGHT", "RA_DOWN"] and value < 0:
                    
                    raise Exception(
                        
                        f"This target only receives positive values from 0 to {DEADZONE_MAX}"
                        
                    )
                
                else:
                    
                    self.__deadzones["analogs"][target] = value
            
            elif target in self.__deadzones["triggers"]:
                
                if value < 0:
                    
                    raise Exception(
                        
                        f"This target only receives positive values from 0 to {DEADZONE_MAX}"
                        
                    )
                    
                else:
                    self.__deadzones["triggers"][target] = value
            
            else:
                
                raise Exception(
                    
                    "Target was not found"
                    
                )
    
    def vibrate(self, duration, strength):
        
        if type(duration) is not int:
            
            raise Exception(
                
                "Duration should be integer"
                
            )
        
        elif duration < 0 or duration > 999999999:
            
            raise Exception(
                
                "Duration should be between (0 to 999999999)"
                
            )
        
        else:
            
            self.__joystick.duration = duration
        
        if type(strength) is not tuple:
            
            raise Exception(
                
                "Strength should be tuple"
                
            )
        
        elif len(strength) > 2:
            
            raise Exception(
                
                "Strength tuple should contain only 2 values"
                
            )
        
        elif [v for v in strength if type(v) is not float]:
            
            raise Exception(
                
                "Strength tuple value should be float"
                
            )
        
        elif [v for v in strength if v > 1.0 or v < 0.0]:
            
            raise Exception(
                
                "Strength tuple value should be between (0.0 to 1.0)"
                
            )
        
        else:
            
            self.__joystick.strengthLeft  = strength[0]
            self.__joystick.strengthRight = strength[1]
        
        try:
            
            self.__joystick.startVibration()
        
        except:
            
            raise Exception(
                
                "Couldn't vibrate joystick"
                
            )
    
    def stopVibration(self):
        
        if self.isVibrating():
            
            try:
                
                self.__joystick.stopVibration()
            
            except:
                
                raise Exception(
                    
                    "Couldn't stop the joystick vibration"
                    
                )
    
    def isVibrating(self):
    
        return self.__joystick.isVibrating
    