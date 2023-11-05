# bge module
import bge

class Mouse:
    
    def __init__(self):
        
        # get mouse
        self.__mouse = bge.logic.mouse
        
        # initialize mouse keys
        self.keys = {
            
            # default buttons
            "LMB" : self.__mouse.inputs[ bge.events.LEFTMOUSE   ],
            "MMB" : self.__mouse.inputs[ bge.events.MIDDLEMOUSE ],
            "RMB" : self.__mouse.inputs[ bge.events.RIGHTMOUSE  ],
            
            # wheel
            "WMU" : self.__mouse.inputs[ bge.events.WHEELUPMOUSE   ],
            "WMD" : self.__mouse.inputs[ bge.events.WHEELDOWNMOUSE ],
            
            # extra buttons
            "MB4" : self.__mouse.inputs[ bge.events.LEFTTHUMBMOUSE  ],
            "MB5" : self.__mouse.inputs[ bge.events.RIGHTTHUMBMOUSE ],
            "MB6" : self.__mouse.inputs[ bge.events.BUTTON6MOUSE    ],
            "MB7" : self.__mouse.inputs[ bge.events.BUTTON7MOUSE    ]
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
                
                "Mouse keys was not initialized"
                
            )
    
    def centralize(self):
        
        try:
            
            self.__mouse.position = (0.5, 0.5)
        
        except:
            
            raise Exception(
                
                "Couldn't center the mouse"
                
            )
    
    @property
    def getPosition(self):
        return self.__mouse.position
    
    @property
    def getDeltaPosition(self):
        return self.__mouse.deltaPosition
    
    def setPosition(self, new_pos):
        
        if type(new_pos) is not tuple:
            
            raise Exception(
                
                "Position should be tuple"
                
            )
        
        elif len(new_pos) > 2:
            
            raise Exception(
                
                "Position tuple should contain only 2 values"
                
            )
        
        elif [v for v in new_pos if type(v) is not float]:
            
            raise Exception(
                
                "Position tuple values should be float"
                
            )
        
        else:
            
            try:
                
                self.__mouse.position = new_pos
            
            except:
                
                raise Exception(
                    
                    "Couldn't set mouse position"
                    
                )
    
    def isCursorActive(self):
        
        return self.__mouse.visible
    
    def showCursor(self, condition):
        
        if type(condition) is not bool:
            
            raise Exception(
                
                "Condition should be boolean"
                
            )
        
        else:
            
            try:
                
                self.__mouse.visible = condition
            
            except:
                
                raise Exception(
                    
                    "Couldn't set cursor visibility"
                    
                )

# mouse instance
m_instance = Mouse()
