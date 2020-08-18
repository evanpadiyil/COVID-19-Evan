import json
import numpy as np
import boto3

from flask import Flask, render_template, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World"
