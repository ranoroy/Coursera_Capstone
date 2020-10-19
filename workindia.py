from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

user_list = {}

@app.route('/user/', methods=['GET','POST'])
def create():
    received_from = request.json
    username = received_from['username']
    password = received_from['password']
    user_list[username] = password
    return jsonify(status = 'account created')

app.run()
