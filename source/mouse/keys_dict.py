from bge import events
from bge.logic import mouse

KEYS = {
    # standard buttons
    "LMB" : mouse.inputs[ events.LEFTMOUSE       ],
    "MMB" : mouse.inputs[ events.MIDDLEMOUSE     ],
    "RMB" : mouse.inputs[ events.RIGHTMOUSE      ],
    
    # wheel buttons
    "WMU" : mouse.inputs[ events.WHEELUPMOUSE    ],
    "WMD" : mouse.inputs[ events.WHEELDOWNMOUSE  ],
    
    # extra buttons
    "MB4" : mouse.inputs[ events.LEFTTHUMBMOUSE  ],
    "MB5" : mouse.inputs[ events.RIGHTTHUMBMOUSE ],
    "MB6" : mouse.inputs[ events.BUTTON6MOUSE    ],
    "MB7" : mouse.inputs[ events.BUTTON7MOUSE    ],
}
