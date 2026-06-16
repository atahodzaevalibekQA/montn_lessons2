class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name 
        self.level = level
        self.health = health
        self.strength = strength
        
    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.level}')
        
    def attack(self):
        print(f'{self.name} наносит удар!')
        self.strength -= 1
        
    def rest(self):
        print(f'{self.name} отдыхает...')
        self.health += 1

Aftandil = Hero("Aftandil", 100, 100, 100)
Alibek = Hero("Alibek", 100, 100, 100)


Aftandil.greet()
print(f'Сила до удара: {Aftandil.strength}')
Aftandil.attack()
print(f'Сила после удара: {Aftandil.strength}') 

Alibek.greet()
print(f'Здоровье до отдыха: {Alibek.health}')
Alibek.rest()
print(f'Здоровье после отдыха: {Alibek.health}') 