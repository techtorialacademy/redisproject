from flask import render_template, request
from app import app, cache
import time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/without_redis')
def without_redis():
    start_time = time.time()
    time.sleep(5)  # Simulating a time-consuming task
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    return f"Fetched in {duration} seconds without Redis."

@app.route('/with_redis')
def with_redis():
    start_time = time.time()

    data = cache.get('data')
    if data is None:
        time.sleep(5)  # Simulating a time-consuming task
        data = "Some Data"
        cache.setex('data', 30, data)

    end_time = time.time()
    duration = round(end_time - start_time, 2)
    return f"Fetched in {duration} seconds with Redis."

