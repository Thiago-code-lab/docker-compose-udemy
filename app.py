import time
import redis
import os
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'<h1>Olá do Docker Compose! 🐳</h1><p>Esta página foi vista {count} vezes.</p>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)