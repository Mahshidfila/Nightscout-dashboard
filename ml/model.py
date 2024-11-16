import numpy as np
from sklearn.linear_model import LinearRegression

def train_model(data):
    time = np.array([entry['dateString'] for entry in data]).reshape(-1, 1)
    glucose = np.array([entry['sgv'] for entry in data])

    model = LinearRegression()
    model.fit(time, glucose)

    return model

def predict_glucose(model, time):
    return model.predict(np.array([[time]])) 
