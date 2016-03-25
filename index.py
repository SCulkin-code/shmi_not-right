from flask import Flask, render_template, request, flash
import json
import os

app = Flask(__name__)

#Needs setting as CSRF_ENABLED=True for flask-wtf. Keep secret_key, secret
app.secret_key = ''

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/node')
def node():
    with open ('graph.json','r') as json_file:
        node_data = json.load(json_file)
    return render_template('node.html', graph_data=node_data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
