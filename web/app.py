from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)
producer_process = None
spark_process = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    global producer_process, spark_process
    if not producer_process:
        producer_process = subprocess.Popen(["python3", "../backend/kafka_producer.py"])
    if not spark_process:
        spark_process = subprocess.Popen(["spark-submit", "../spark/streaming_job.py"])
    return redirect(url_for('index'))

@app.route('/stop')
def stop():
    global producer_process, spark_process
    if producer_process:
        producer_process.terminate()
        producer_process = None
    if spark_process:
        spark_process.terminate()
        spark_process = None
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)