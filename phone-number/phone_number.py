class Phone(object):
    
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.number = self.sanitizer(self.phone_number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:]
             
    def sanitizer(self,tel):
        data = [d for d in tel if d.isalnum()]   
        digits = int(len(data))   
        if digits < 10:
            raise ValueError("The digit cannot be below 10")

        if digits > 11:
            raise ValueError("Digits cannot be greater than 11")
            
        if digits == 11:
            
            if data[0] != str(1):
                raise ValueError("Error occured,none one is not acepted as the starting digit in 11 digit")
                
            else:
                data.pop(0)            
                
        if data[0] == str(0) or data[0] == str(1):
            raise ValueError("The area code cannot start with 0 or 1")

        if data[3] == str(0) or data[3] == str(1):
            raise ValueError ("The exec-code cannot start with 0 or 1")
        else:
            return "".join(data)
       
           
    
    def pretty(self):
         
        return ("({}) {}-{}".format(self.area_code,self.exchange_code,self.subscriber_number))            
      


