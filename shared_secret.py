#implementation of shared secret


import random


class User():
    def __init__(self, name):
        self.clock_size = 571
        self.base = 7
        self.name = name
        self.__private = random.randint(0, self.clock_size)
        self._ppn = (self.base ** self.__private) % self.clock_size
        self.__shared = None
    
    def gen_shared_secret(self, other):
        self.__shared = ":0<3d".format((other._ppn ** self.__private) % self.clock_size)
        other.__shared = ":0<3d".format((self._ppn ** other.__private) % other.clock_size)
        
    
    
def main():
    me = User('me')
    other = User('arnold')
    me.gen_shared_secret(other)
    
main()