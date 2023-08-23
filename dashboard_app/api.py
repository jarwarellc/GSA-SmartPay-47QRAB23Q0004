# dashboard_app/api.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/data")
def fetch_data():
    # JarWare Developer: Simulate fetching programmatic data from a database
    return [
        {"name": "Agency A", "value": 1000000},
        {"name": "Agency B", "value": 750000},
    ]  # Placeholder for actual data retrieval logic
