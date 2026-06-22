from abc import ABC, abstractmethod


class Hero(ABC):
    
    
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength
        
    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.level} ')
        
    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1
        
    @abstractmethod
    def attack(self):
       pass
   
   
class Warrior(Hero):
    
    def attack(self):
        print("Воин атакует мечом")
        

class Mage(Hero):
    
    def attack(self):
        print("Маг использует магию")
        
        
class Assassin(Hero):
    
    def attack(self):
        print("Ассасин атакует из под тишка")
        
        
warrior = Warrior("Алиба", 1, 2, 3)
mage = Mage("Afta", 1, 2, 3)
assassin = Assassin("Isak", 1, 2, 3)


warrior.attack()
warrior.greet()
warrior.rest()


mage.attack()
mage.rest()
mage.greet()

assassin.greet()
assassin.attack()
assassin.rest()
        