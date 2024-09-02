class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

singleton1 = Singleton("First")
singleton2 = Singleton("Second")

print(singleton1.value)  # Output: First
print(singleton2.value)  # Output: First
