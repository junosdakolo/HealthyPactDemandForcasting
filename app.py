from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os
from prophet import Prophet

app = Flask(__name__)

# Load the trained Prophet model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "✅ HealthyPact Demand Forecasting API is live!"

@app.route('/forecast', methods=['POST'])
def forecast():
    try:
        input_data = request.get_json()
        # Use environment variable or default value
        periods = int(input_data.get("periods", os.getenv("DEFAULT_PERIODS", 6)))

        # Prepare future dataframe
        future = model.make_future_dataframe(periods=periods, freq='M')

        # Use average of last 6 rows for each regressor
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
        return jsonify({"error": str(e)})

# Only used when testing locally
if __name__ == '__main__':
    app.run(debug=True)
