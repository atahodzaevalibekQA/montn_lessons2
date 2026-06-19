import random
import string


class BankAccount:
    
    def __init__(self, login, password, balance):
        self.login = login
        self.__password = password
        self._balance = balance
        
    def get_user_balance(self, password):
        if password == self.__password:
            return self._balance
        else:
            return "Не верный пароль"
        
        
    def __random_pass(self):
        data = string.ascii_letters + string.digits
        password = ''.join(random.choice(data) for _ in range(6))
        return password
    
    def get_random_pass(self):
        return self.__random_pass()
        
        
    
        

#ardager = BankAccount("Ardager", "123122", 1000)

from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def move(self):
        pass
    
    
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
     def move(self):
         return super().move()
     
     def make_sound(self):
         return super().make_sound()





