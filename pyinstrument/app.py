from flask import Flask, jsonify

from pyinstrument import Profiler

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "container-apps-python-profilers-pyinstrument"})

@app.route("/fib/console")
def fib_console():
    profiler = Profiler()
    profiler.start()

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

    profiler.stop()
    print(profiler.output_text(unicode=True, color=True))
    return jsonify({"message": "Running Fibonacci sequence.."})

@app.route("/fib/html")
def fib_html():
    profiler = Profiler()
    profiler.start()

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

    profiler.stop()
    p = profiler.output_html("profile.html")
    return p
