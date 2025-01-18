class victim:
    def __init__(self, password, name, pin, ip, other):
        self.password = password ; self.name = name ; self.pin = pin ;self.ip = ip ; self.other = other
        #self.other is an list
    def verify(self, password, pin):
        if self.pin == pin and self.password == password: return True
        else: return False
    #
if __name__ == '__main__':
    pass