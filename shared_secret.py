#implementation of shared secret


import random


class User():
    def __init__(self, name):
        self.clock_size = 571
        self.base = 7
        self.name = name
        self.__private = random.randint(0, self.clock_size)
        self._ppn = (self.base ** self.__private) % self.clock_size
        self.__shared = []
    
    def gen_shared_secret(self, other):
        self.__shared.append(":0<3d".format((other._ppn ** self.__private) % self.clock_size))
        other.__shared.append(":0<3d".format((self._ppn ** other.__private) % other.clock_size))
        
    
    
def main():
    me = User('me')
    other = User('arnold')
    #when the user sends a message
    me.__shared = []
    for i in range(message//4):
        me.gen_shared_secret(other)
    
main()