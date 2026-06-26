class Math:
    
    
    @staticmethod
    def __add__(a, b):
        return a + b
    
print(Math.__add__(5, 3))



class Bank:
    name = 'Mbank'
    
    def __init__(self, value):
        self.value = value
        
    def get_value(self):
        return self.value
    
    @classmethod
    def get_name(cls):
        return cls.name
    
    @classmethod
    def base_create(cls):
        return cls("Base value")
        
    
    
bank = Bank("Ardager")
bank1 = Bank.base_create()

#print(bank.get_value())
#print(bank.get_name())
#print(bank1.get_value())
#print(bank1.get_name())


class Product:
    def __init__(self, price):
        self.__price = price # Переменная защищена (два подчеркивания)
        
    @property
    def price(self):
        """Возвращает значение price."""
        return self.__price
    
    @price.setter
    def price(self, value):
        """Проверяет значение перед установкой."""
        if value < 0:
            raise ValueError("Цена не может быть отрицательной!!")
        self.__price = value

iphone = Product(1250)

# 1. Мы используем .price как свойство, а не как функцию с ()
print(iphone.price) 

# 2. Когда мы присваиваем значение, срабатывает @price.setter
iphone.price = 200 # Ок
# iphone.price = -50 # Вызовет ошибку ValueError, так как setter не пропустит

# print(iphone.price)
# print(iphone.get_price())
# print(iphone.__price)



def simple_decorator(func):
    def wrapper():
        print("До выполнения")
        func()
        print("после выполнения")
    return wrapper


@simple_decorator
def say_hello():
    print("Hello kitty")
   
   
say_hello()
   

        
    
    

