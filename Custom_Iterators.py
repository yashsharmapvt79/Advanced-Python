class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        a, self.a, self.b = self.a, self.b, self.a + self.b
        return a

for number in Fibonacci():
    if number > 50:
        break
    print(number)
