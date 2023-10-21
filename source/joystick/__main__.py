from bge.logic import joysticks as joysticks_list
from .joystick_class import Joystick

class Joysticks:
    def __init__(self):
        self.keys = {
            0 : Joystick(0),
            1 : Joystick(1),
            2 : Joystick(2),
            3 : Joystick(3),
            4 : Joystick(4),
            5 : Joystick(5),
            6 : Joystick(6),
            7 : Joystick(7),
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
                f'~Key Accessing~ >> Keys was not initialized correctly'
            )
    
    def listAll(self):
        print( joysticks_list )

joysticks = Joysticks()
