# HealthyPact Demand Forecasting API

This project is a demand forecasting REST API built with **Flask** and deployed on **Render**. It uses **Facebook Prophet** to predict future product demand based on historical sales data and economic indicators.

---

## Live API

**Home Route**  
`GET https://healthypactdemandforcasting-1.onrender.com/`  
Returns a message confirming the API is live.

**Forecast Endpoint**  
`POST https://healthypactdemandforcasting-1.onrender.com/forecast`  
Accepts a JSON payload with the number of future months to forecast.  
Returns forecasted demand for the next `n` months.

### Sample Request (JSON)
```json
{
  "periods": 6
}
```

---

## Project Structure

```
BusinessModel/
├── app.py              # Flask app with forecast endpoint
├── model.pkl           # Trained Prophet model
├── requirements.txt    # Python dependencies
├── render.yaml         # Render deployment config
├── test_forecast_api.py # Python script to test the API
```

---

## Deployment (via Render)

1. Push code to GitHub
2. Log in to [https://render.com](https://render.com)
3. Create new Web Service from GitHub
4. **Root Directory**: `/BusinessModel`
5. **Build Command**: `pip install -r requirements.txt`
6. **Start Command**: `gunicorn app:app`
7. Deploy and test live!

---

## Test the API

### Option 1: Python (test_forecast_api.py)
```bash
python test_forecast_api.py
```


## Environment Notes

- Python 3.11
- Flask
- Prophet
- gunicorn
- joblib

---

## License

This project is created as part of the final Business Analytics project for Nexford University. You may adapt or extend it for educational or demonstration purposes.

---

## Author

**Dakolo Emmanuel Imomotimi**  
Email: edakolo@learner.nexford.ord 
Nexford University · Master's in Data Analytics