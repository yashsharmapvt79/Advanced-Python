import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

# Example data: Daily temperature data
data = pd.DataFrame({
    'ds': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'y': pd.Series(range(100)) + 10 * np.sin(np.linspace(0, 3.14, 100))
})

# Initialize Prophet model
model = Prophet()
model.fit(data)

# Create future dataframe
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Plot the forecast
fig = model.plot(forecast)
plt.show()
