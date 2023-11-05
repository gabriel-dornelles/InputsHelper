# bge module
import bge

class Keyboard:
    
    def __init__(self):
        
        self.keys = {
            
            # alphabet
            "A" : bge.logic.keyboard.inputs[ bge.events.AKEY ],
            "B" : bge.logic.keyboard.inputs[ bge.events.BKEY ],
            "C" : bge.logic.keyboard.inputs[ bge.events.CKEY ],
            "D" : bge.logic.keyboard.inputs[ bge.events.DKEY ],
            "E" : bge.logic.keyboard.inputs[ bge.events.EKEY ],
            "F" : bge.logic.keyboard.inputs[ bge.events.FKEY ],
            "G" : bge.logic.keyboard.inputs[ bge.events.GKEY ],
            "H" : bge.logic.keyboard.inputs[ bge.events.HKEY ],
            "I" : bge.logic.keyboard.inputs[ bge.events.IKEY ],
            "J" : bge.logic.keyboard.inputs[ bge.events.JKEY ],
            "K" : bge.logic.keyboard.inputs[ bge.events.KKEY ],
            "L" : bge.logic.keyboard.inputs[ bge.events.LKEY ],
            "M" : bge.logic.keyboard.inputs[ bge.events.MKEY ],
            "N" : bge.logic.keyboard.inputs[ bge.events.NKEY ],
            "O" : bge.logic.keyboard.inputs[ bge.events.OKEY ],
            "P" : bge.logic.keyboard.inputs[ bge.events.PKEY ],
            "Q" : bge.logic.keyboard.inputs[ bge.events.QKEY ],
            "R" : bge.logic.keyboard.inputs[ bge.events.RKEY ],
            "S" : bge.logic.keyboard.inputs[ bge.events.SKEY ],
            "T" : bge.logic.keyboard.inputs[ bge.events.TKEY ],
            "U" : bge.logic.keyboard.inputs[ bge.events.UKEY ],
            "V" : bge.logic.keyboard.inputs[ bge.events.VKEY ],
            "W" : bge.logic.keyboard.inputs[ bge.events.WKEY ],
            "X" : bge.logic.keyboard.inputs[ bge.events.XKEY ],
            "Y" : bge.logic.keyboard.inputs[ bge.events.YKEY ],
            "Z" : bge.logic.keyboard.inputs[ bge.events.ZKEY ],
            
            # alphanumeric numbers
            "alpha0" : bge.logic.keyboard.inputs[ bge.events.ZEROKEY  ],
            "alpha1" : bge.logic.keyboard.inputs[ bge.events.ONEKEY   ],
            "alpha2" : bge.logic.keyboard.inputs[ bge.events.TWOKEY   ],
            "alpha3" : bge.logic.keyboard.inputs[ bge.events.THREEKEY ],
            "alpha4" : bge.logic.keyboard.inputs[ bge.events.FOURKEY  ],
            "alpha5" : bge.logic.keyboard.inputs[ bge.events.FIVEKEY  ],
            "alpha6" : bge.logic.keyboard.inputs[ bge.events.SIXKEY   ],
            "alpha7" : bge.logic.keyboard.inputs[ bge.events.SEVENKEY ],
            "alpha8" : bge.logic.keyboard.inputs[ bge.events.EIGHTKEY ],
            "alpha9" : bge.logic.keyboard.inputs[ bge.events.NINEKEY  ],
            
            # modifiers keys
            "CapsLock"     : bge.logic.keyboard.inputs[ bge.events.CAPSLOCKKEY   ],
            "RightControl" : bge.logic.keyboard.inputs[ bge.events.RIGHTCTRLKEY  ],
            "LeftControl"  : bge.logic.keyboard.inputs[ bge.events.LEFTCTRLKEY   ],
            "LeftAlt"      : bge.logic.keyboard.inputs[ bge.events.LEFTALTKEY    ],
            "RightAlt"     : bge.logic.keyboard.inputs[ bge.events.RIGHTALTKEY   ],
            "RightShift"   : bge.logic.keyboard.inputs[ bge.events.RIGHTSHIFTKEY ],
            "LeftShift"    : bge.logic.keyboard.inputs[ bge.events.LEFTSHIFTKEY  ],
            
            # arrow keys
            "UpArrow"    : bge.logic.keyboard.inputs[ bge.events.UPARROWKEY    ],
            "DownArrow"  : bge.logic.keyboard.inputs[ bge.events.DOWNARROWKEY  ],
            "LeftArrow"  : bge.logic.keyboard.inputs[ bge.events.LEFTARROWKEY  ],
            "RightArrow" : bge.logic.keyboard.inputs[ bge.events.RIGHTARROWKEY ],
            
            # numpad keys
            "Pad0"        : bge.logic.keyboard.inputs[ bge.events.PAD0        ],
            "Pad1"        : bge.logic.keyboard.inputs[ bge.events.PAD1        ],
            "Pad2"        : bge.logic.keyboard.inputs[ bge.events.PAD2        ],
            "Pad3"        : bge.logic.keyboard.inputs[ bge.events.PAD3        ],
            "Pad4"        : bge.logic.keyboard.inputs[ bge.events.PAD4        ],
            "Pad5"        : bge.logic.keyboard.inputs[ bge.events.PAD5        ],
            "Pad6"        : bge.logic.keyboard.inputs[ bge.events.PAD6        ],
            "Pad7"        : bge.logic.keyboard.inputs[ bge.events.PAD7        ],
            "Pad8"        : bge.logic.keyboard.inputs[ bge.events.PAD8        ],
            "Pad9"        : bge.logic.keyboard.inputs[ bge.events.PAD9        ],
            "PadPeriod"   : bge.logic.keyboard.inputs[ bge.events.PADPERIOD   ],
            "PadSlash"    : bge.logic.keyboard.inputs[ bge.events.PADSLASHKEY ],
            "PadAsterisk" : bge.logic.keyboard.inputs[ bge.events.PADASTERKEY ],
            "PadMinus"    : bge.logic.keyboard.inputs[ bge.events.PADMINUS    ],
            "PadEnter"    : bge.logic.keyboard.inputs[ bge.events.PADENTER    ],
            "PadPlus"     : bge.logic.keyboard.inputs[ bge.events.PADPLUSKEY  ],
            
            # function keys
            "F1"  : bge.logic.keyboard.inputs[ bge.events.F1KEY  ],
            "F2"  : bge.logic.keyboard.inputs[ bge.events.F2KEY  ],
            "F3"  : bge.logic.keyboard.inputs[ bge.events.F3KEY  ],
            "F4"  : bge.logic.keyboard.inputs[ bge.events.F4KEY  ],
            "F5"  : bge.logic.keyboard.inputs[ bge.events.F5KEY  ],
            "F6"  : bge.logic.keyboard.inputs[ bge.events.F6KEY  ],
            "F7"  : bge.logic.keyboard.inputs[ bge.events.F7KEY  ],
            "F8"  : bge.logic.keyboard.inputs[ bge.events.F8KEY  ],
            "F9"  : bge.logic.keyboard.inputs[ bge.events.F9KEY  ],
            "F10" : bge.logic.keyboard.inputs[ bge.events.F10KEY ],
            "F11" : bge.logic.keyboard.inputs[ bge.events.F11KEY ],
            "F12" : bge.logic.keyboard.inputs[ bge.events.F12KEY ],
            "F13" : bge.logic.keyboard.inputs[ bge.events.F13KEY ],
            "F14" : bge.logic.keyboard.inputs[ bge.events.F14KEY ],
            "F15" : bge.logic.keyboard.inputs[ bge.events.F15KEY ],
            "F16" : bge.logic.keyboard.inputs[ bge.events.F16KEY ],
            "F17" : bge.logic.keyboard.inputs[ bge.events.F17KEY ],
            "F18" : bge.logic.keyboard.inputs[ bge.events.F18KEY ],
            "F19" : bge.logic.keyboard.inputs[ bge.events.F19KEY ],
            
            # other keys
            "AccentGrave"  : bge.logic.keyboard.inputs[ bge.events.ACCENTGRAVEKEY  ],
            "BackSlash"    : bge.logic.keyboard.inputs[ bge.events.BACKSLASHKEY    ],
            "BackSpace"    : bge.logic.keyboard.inputs[ bge.events.BACKSPACEKEY    ],
            "Comma"        : bge.logic.keyboard.inputs[ bge.events.COMMAKEY        ],
            "Delete"       : bge.logic.keyboard.inputs[ bge.events.DELKEY          ],
            "End"          : bge.logic.keyboard.inputs[ bge.events.ENDKEY          ],
            "Equal"        : bge.logic.keyboard.inputs[ bge.events.EQUALKEY        ],
            "Esc"          : bge.logic.keyboard.inputs[ bge.events.ESCKEY          ],
            "Home"         : bge.logic.keyboard.inputs[ bge.events.HOMEKEY         ],
            "Insert"       : bge.logic.keyboard.inputs[ bge.events.INSERTKEY       ],
            "LeftBracket"  : bge.logic.keyboard.inputs[ bge.events.LEFTBRACKETKEY  ],
            "LineFeed"     : bge.logic.keyboard.inputs[ bge.events.LINEFEEDKEY     ],
            "Minus"        : bge.logic.keyboard.inputs[ bge.events.MINUSKEY        ],
            "PageDown"     : bge.logic.keyboard.inputs[ bge.events.PAGEDOWNKEY     ],
            "PageUp"       : bge.logic.keyboard.inputs[ bge.events.PAGEUPKEY       ],
            "PauseBreak"   : bge.logic.keyboard.inputs[ bge.events.PAUSEKEY        ],
            "Period"       : bge.logic.keyboard.inputs[ bge.events.PERIODKEY       ],
            "Quote"        : bge.logic.keyboard.inputs[ bge.events.QUOTEKEY        ],
            "RightBracket" : bge.logic.keyboard.inputs[ bge.events.RIGHTBRACKETKEY ],
            "Enter"        : bge.logic.keyboard.inputs[ bge.events.ENTERKEY        ],
            "SemiColon"    : bge.logic.keyboard.inputs[ bge.events.SEMICOLONKEY    ],
            "Slash"        : bge.logic.keyboard.inputs[ bge.events.SLASHKEY        ],
            "Space"        : bge.logic.keyboard.inputs[ bge.events.SPACEKEY        ],
            "Tab"          : bge.logic.keyboard.inputs[ bge.events.TABKEY          ]
            
        }
    
    def __getitem__(self, key):
        
        if hasattr(self, "keys"):
            
            try:
                
                return self.keys[key]
            
            except:
                
                "Couldn't acess the given key"
        
        else:
            
            raise Exception(
                
                "Keyboard keys was not initialized"
                
            )

# keyboard instance
k_instance = Keyboard()
