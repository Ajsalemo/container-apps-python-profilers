from flask import Flask, jsonify

import cProfile, pstats, io
from pstats import SortKey

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "container-apps-python-profilers-cProfile"})

@app.route("/fib")
def fib():
    pr = cProfile.Profile()
    pr.enable()
    def fibonacci(n):
        if n < 0:
            print("Incorrect input")    
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
        
    fibonacci(20)

    pr.disable()

    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.dump_stats("/app/profiles/profile.txt")

    return jsonify({"message": "Running Fibonacci sequence.."})