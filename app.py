from flask import Flask, render_template, jsonify
from gaze_module.detect import start_detection, get_detection_results

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    start_detection()
    return jsonify({"status": "Detection started"})

@app.route('/results')
def results():
    data = get_detection_results()
    return jsonify(data)

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/reset')
def reset():
    from gaze_module.detect import results_data
    results_data["blinks"] = 0
    results_data["gaze"] = []
    results_data["stress"] = []
    results_data["timestamps"] = []
    return jsonify({"status": "Detection reset"})

if __name__ == '__main__':
    app.run(debug=True)
