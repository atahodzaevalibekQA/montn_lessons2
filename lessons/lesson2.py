class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        
    def action(self):
        return f"{self.name} base action!!"
    
    
class MageHero(Hero):
    
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    
    def action(self):
        return f"This new action "
    

kirito = Hero("Kirito", 100, 1000)
gendalf_silver = MageHero("Gendalf", 100, 1000, 10)

#print(kirito.action())
#print(gendalf_silver.action())


class Fly:
    
    def f_action(self):
        return "Fly"
    
    
class Swim:
    def s_action(self):
        return "Swim"
    
    
class Animal(Swim, Fly):
    
    def action(self):
        return 'action'
    
    
donald_duck = Animal()
#print(donald_duck.action())
#print(donald_duck.f_action())
#print(donald_duck.s_action())


class A:
    def action(self):
        print("A")


class B(A):
    def action(self):
        super().action()
        print("B")


class C(A):
    def action(self):
        super().action()
        print("C")


class D(B, C):
    def action(self):
        super().action()
        print("D")


test_obj = D()

test_obj.action()

# print("\n--- Список MRO для класса D: ---")
# for cls in D.mro():
#     print(cls)