from flask import Flask, request, jsonify
import pandas as pd
import joblib
from prophet import Prophet
import os

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return "HealthyPact Demand Forecasting API is live!"

@app.route('/forecast', methods=['POST'])
def forecast():
    try:
        data = request.get_json()

        # Get number of future periods from input or use default
        periods = int(data.get("periods", 6))

        # Create future dataframe
        future = model.make_future_dataframe(periods=periods, freq='M')

        # Use average of most recent months for regressor values
        recent = model.history[['CPI', 'Campaigns', 'Holidays']].tail(6).mean()
        future['CPI'] = recent['CPI']
        future['Campaigns'] = recent['Campaigns']
        future['Holidays'] = recent['Holidays']

        # Generate forecast
        forecast = model.predict(future)

        result = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods).to_dict(orient='records')

        return jsonify({
            "forecast": result,
            "message": f"Forecast generated for next {periods} months"
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Only run locally
if __name__ == '__main__':
    app.run(debug=True)
