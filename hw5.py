import time

class User:
    
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
        
admin = User("Ardager", "admin")

user = User("Bek", "user")       
        
        
def is_admin(func):
    
    def wrapper(user):
        if user.role == "admin":
            return func(user)
        return "У вас нет доступа"
    return wrapper

@is_admin
def delete_video(user):
    return "Видео удалено"


def timer(func):
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция '{func.__name__}' выполнялась: {execution_time:.4f} секунд")
        
        return result
    
    return wrapper

@timer
def download_video():
    time.sleep(2)
    return "Видео загружено"


download_video()
print(delete_video(admin)) # Админ удаляет
print(delete_video(user))  # Обычный юзер пытается удалить


