from flask import Flask
import redis

redis = redis.Redis(host='redis-server', port=6379, db=0, decode_responses=True)
print('Successfully connected to Redis!')
redis.set('counter', 0)

app = Flask(__name__)
@app.route("/")
def hello_world():
    redis.incr('counter')
    return f"<p>Hello, World! This site has been visited {redis.get('counter')} times!</p>"