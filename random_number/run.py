from flask import Flask, jsonify, render_template, request
from random import randrange
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/echo/', methods=['GET'])
def echo():
    number = randrange(1,100)
    ret_data = {"value": number}
    return jsonify(ret_data)
 
if __name__ == '__main__':
    app.run(port=8080, debug=True)
