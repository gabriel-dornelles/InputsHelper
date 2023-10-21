class AxisClass:
    def __init__(self, device, axis):
        # mouse device
        self.__device = device
        
        # mouse axis
        self.__axis = axis
        
        # mouse old position
        self.__positiveOldPosition = self.__device.position
        self.__negativeOldPosition = self.__positiveOldPosition

    @property
    def positive(self):
        if self.__device.position[self.__axis] != self.__positiveOldPosition:
            if self.__device.position[self.__axis] > self.__positiveOldPosition[self.__axis]:
                self.__positiveOldPosition = self.__device.position
                return True
            else:
                self.__positiveOldPosition = self.__device.position
                return False
    
    @property
    def negative(self):
        if self.__device.position[self.__axis] != self.__negativeOldPosition:
            if self.__device.position[self.__axis] < self.__negativeOldPosition[self.__axis]:
                self.__negativeOldPosition = self.__device.position
                return True
            else:
                self.__negativeOldPosition = self.__device.position
                return False
