from flask import Flask, request, jsonify
import pandas as pd
import joblib
from prophet import Prophet

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "✅ HealthyPact Demand Forecasting API is live!"

@app.route('/forecast', methods=['POST'])
def forecast():
    try:
        input_data = request.get_json()
        periods = int(input_data.get("periods", 6))

        future = model.make_future_dataframe(periods=periods, freq='M')
        recent = model.history[['CPI', 'Campaigns', 'Holidays']].tail(6).mean()
        future['CPI'] = recent['CPI']
        future['Campaigns'] = recent['Campaigns']
        future['Holidays'] = recent['Holidays']

        forecast = model.predict(future)
        result = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods).to_dict(orient='records')

        return jsonify({
            "forecast": result,
            "message": f"Forecast generated for next {periods} months."
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)