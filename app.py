from flask import Flask, render_template, jsonify, request
from redis import Redis

app = Flask(__name__)
redis = Redis()

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/set/<int:value>')
def set(value):
    '''Set the value of testfield in the Redis DB (0 or 1).'''
    return jsonify(response=redis.set('testfield', value))

@app.route('/query')
def query():
    '''Fetch a value from Redis.'''
    name = request.args.get('name', '', type=str)
    return jsonify(value=redis.get(name).decode('utf-8'))

