from flask import Flask
import redis

app = Flask(__name__)
cache = redis.StrictRedis(host='your-redis-endpoint.amazonaws.com', port=6379, db=0, decode_responses=True)

from app import routes

