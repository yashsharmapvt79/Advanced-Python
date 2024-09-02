class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['greeting'] = 'Hello, world!'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass().greeting)  # Output: Hello, world!
