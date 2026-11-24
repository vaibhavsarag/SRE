from pickletools import read_string1
from turtle import home

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message':'welcome to my first flask api!!'})

@app.route('/users', methods =['GET'])
def get_users():
    users:[{"id":1, "name":"Raj"},
           {"id":2, "name":"Priya"}] # type: ignore
    return jsonify(users)

if __name__=='__main__':
    app.run(debug=True, port=5000)