import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# example
data = {
    "time": [1, 2, 3, 4, 5], 
    "glucose_level": [120, 130, 125, 140, 135]
}
df = pd.DataFrame(data)

X = df["time"].values.reshape(-1, 1) 
y = df["glucose_level"].values

model = LinearRegression()
model.fit(X, y)

future_times = np.array([6, 7, 8]).reshape(-1, 1)
predictions = model.predict(future_times)

plt.plot(df["time"], df["glucose_level"], label="داده‌های واقعی")
plt.plot(future_times, predictions, label="پیش‌بینی", linestyle='--')
plt.xlabel("زمان")
plt.ylabel("مقدار قند خون")
plt.title("پیش‌بینی قند خون")
plt.legend()
plt.show()
