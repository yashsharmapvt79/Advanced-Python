import concurrent.futures
import time

def compute_square(number):
    time.sleep(1)
    return number * number

numbers = [1, 2, 3, 4, 5]

# Use ThreadPoolExecutor to perform concurrent processing
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(compute_square, numbers))

print("Results:", results)
