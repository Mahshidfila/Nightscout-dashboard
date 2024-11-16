from flask import Flask, render_template
from data.nightscout_data import get_nightscout_data
from ml.model import train_model, predict_glucose

app = Flask(__name__)

# URL Nightscout
API_URL = "http://your-nightscout-instance-url"

@app.route('/')
def index():
    data = get_nightscout_data(API_URL)
    
    if data is not None:
        model = train_model(data)

        prediction = predict_glucose(model, 1625244000000) 
        
        return render_template('index.html', data=data, prediction=prediction)
    else:
        return "Error fetching data from Nightscout"

if __name__ == '__main__':
    app.run(debug=True)
