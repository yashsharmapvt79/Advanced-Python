import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Value': [10, 20, 15, 25]
}
df = pd.DataFrame(data)

# Plot the data
df.plot(x='Name', y='Value', kind='bar', legend=False)
plt.xlabel('Name')
plt.ylabel('Value')
plt.title('Bar Chart of Values')
plt.show()
