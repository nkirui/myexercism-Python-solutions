import random
import string
import re


class Robot:

    
    
    def __init__(self):
        self.oldname = set()
        self.name = self.generate()

    
    def generate(self):
        
        letters = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
        digits = random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)

        x1 = letters+digits
        name  = re.findall(r'^[A-Z]{2}\d{3}$',x1)

        while "".join(name) not in self.oldname:
            self.oldname.add("".join(name))
       
        
    def reset(self):
        self.name = self.generate()
        

