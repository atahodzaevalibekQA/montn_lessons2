import random


class Hero:
    
    def __init__(self, name, level, health, strength):
        self.name = name
        self.health = health
        self.level = level 
        self.strength = strength
        
    def greet(self):
        print("Привет мой юный друг")
        
    def attack(self):
        print("Наносит удар")
        
    def rest(self):
        print("Герой отдыхает и наносит удар")
        
        
class Warrior(Hero):
    
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina
        
    def attack(self):
        print("Воин атакует мечом")
        
    
class Mage(Hero):
    
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
        
    def attack(self):
        print("Маг кастует заклинание!")
        
        
class Assasin(Hero):
    
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
        
    def attack(self):
        print("Ассасин атакует из под тишка!")
        
        
Alibek = Warrior("Alibek", 10, 10, 10, 10)
Aftandil = Mage("Aftandil", 10, 10, 10, 10)
Islam = Assasin("Islam", 10, 10, 10, 10)

my_values = ["Assasin", "Mage", "Warrior"]

user_choice = input("Выберите героя: Warrior / Mage / Assasin")

comp_choice = random.choice(my_values)

rules = {
    "Warrior": "Assassin",
    "Assassin": "Mage",
    "Mage": "Warrior"
}

if user_choice == comp_choice:
    print("Ничья!")
elif rules[user_choice] == comp_choice:
    print(f"{user_choice} победил!")
else:
    print(f"{comp_choice} победил!")

    

