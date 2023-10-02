from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)


def make_big_array():
    return np.zeros((5000, 5000, 50))


def make_two_arrays():
    arr1 = np.zeros((5000, 5000, 50))
    arr2 = np.ones((5000, 5000, 50))
    return arr1, arr2


@app.route("/")
def index():
    return jsonify({"message": "container-apps-python-profilers-memory_profiler"})

@app.route("/mem")
def mem():
    make_two_arrays()
    make_big_array()    

    return jsonify({"message": "Allocating memory.."})



