from flask import Flask
from pymemcache.client import base
import mysql.connector
import pika

app = Flask(__name__)

# Initialize Memcached client
memcached_client = base.Client(('memcached_server', 11211))
memcached_client.set('test_key', "Ogechukwu says: 'In the world of possibilities, love and innovation create magic!'")

@app.route('/')
def home():
    return f"Hello from the Multi-Container App! {memcached_client.get('test_key').decode('utf-8')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)