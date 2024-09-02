from functools import reduce
from itertools import accumulate

numbers = [1, 2, 3, 4, 5]

# Using `reduce` to calculate the product
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)

# Using `accumulate` to get cumulative sums
cumulative_sum = list(accumulate(numbers))
print("Cumulative sum:", cumulative_sum)
