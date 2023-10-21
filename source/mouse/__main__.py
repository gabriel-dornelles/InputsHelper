from  bge.logic  import mouse
from .keys_dict  import KEYS
from .axis_class import AxisClass

# main class
class MouseClass:
    
    def __init__(self):
        # get mouse
        self.mouse = mouse
        
        # initialize mouse keys
        self.keys = KEYS
        
        # adding X & Y axis to keys dictionary
        self.keys['X_AXIS'] = AxisClass(self.mouse, 0)
        self.keys['Y_AXIS'] = AxisClass(self.mouse, 1)
    
    def __getitem__(self, key):
        if hasattr(self, "keys"):
            try:
                return self.keys[key]
            except:
                raise Exception(
                    f'~Key Accessing~ >> An error occurred while returning the given key, check if the key exists and try again'
                )
        else:
            raise Exception(
                f'~Key Accessing~ >> Mouse keys were not initialized correctly!'
            )
    
    def centralize(self):
        try:
            self.mouse.position = (0.5, 0.5)
        except:
            raise Exception(
                f'~centralize function~~ >> Error centering the mouse'
            )
    
    @property
    def position(self):
        try:
            return self.mouse.position
        except:
            raise Exception(
                f'~position function~ >> Error when trying to return the mouse position!'
            )
    
    @property
    def deltaPosition(self):
        try:
            return self.mouse.deltaPosition
        except:
            raise Exception(
                f'~deltaPosition function~ >> Error when trying to return the mouse delta position!'
            )
    
    def setPosition(self, x, y):
        if type(x) == float and type(y) == float:
            try:
                self.mouse.position = (x, y)
            except:
                raise Exception(
                    f'~setPosition function~ >> Error when setting the mouse position!'
                )
        else:
            raise Exception(
                f'~setPosition function~ >> Invalid parameters type!'
            )
    
    def isCursorActive(self):
        if self.mouse.visible:
            return True
        else:
            return False
    
    def showCursor(self, condition):
        if type(condition) == bool:
            try:
                self.mouse.visible = condition
            except:
                raise Exception(
                    f'~showCursor function~ >> Error when trying to change cursor visibility!'
                )
        else:
            raise Exception(
                f'~showCursor function~ >> Invalid parameter type!'
            )

# mouse instance
mouse = MouseClass()
