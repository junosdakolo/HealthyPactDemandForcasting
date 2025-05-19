import requests

# ✅ Live API URL from Render
url = "https://healthypactdemandforcasting-1.onrender.com/forecast"

# Payload for forecasting 6 months
data = {
    "periods": 6
}

headers = {
    "Content-Type": "application/json"
}

# Make POST request
response = requests.post(url, json=data, headers=headers)

# Print results
print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())