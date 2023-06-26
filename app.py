from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>!!!Deploy a Flask Application to a Kubernetes Cluster using Jenkins and ArgoCD successfully!!!! </h1>'
