from flask import Flask, jsonify
import linecache
import tracemalloc

app = Flask(__name__)

def display_top(snapshot, key_type='lineno', limit=10):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        print("#%s: %s:%s: %.1f KiB"
              % (index, frame.filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))

@app.route("/")
def index():
    return jsonify({"message": "container-apps-python-profilers-tracemallac"})

@app.route("/mem")
def mem():
    tracemalloc.start() 

    for i in range(100):
        o = [0] * i

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 10 ]") 
    for stat in top_stats[:10]:
        print(stat)

    return jsonify({"message": "Allocating memory.."})


@app.route("/mem/prettytop")
def mem_prettytop():
    tracemalloc.start() 

    for i in range(100):
        o = [0] * i

    snapshot = tracemalloc.take_snapshot()
    display_top(snapshot)
    
    return jsonify({"message": "Allocating memory.."})

@app.route("/mem/dumpfile")
def mem_dumpfile():
    tracemalloc.start() 

    for i in range(100):
        o = [0] * i

    snapshot = tracemalloc.take_snapshot()
    snapshot.dump("/app/profiles/snap.out")
    
    return jsonify({"message": "Allocating memory.."})