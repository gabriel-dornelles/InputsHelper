from .keys_dict import KEYS

# main class
class Keyboard:
    def __init__(self):
        self.keys = KEYS
    
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
                f'~Key Accessing~ >> Keyboard keys were not initialized correctly!'
            )
            
keyboard = Keyboard()
