from flask import Flask, redirect, render_template, request, session

# jsonify
# from multiprocessing import Value

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
dev = True
app.count = 0

@app.route('/')
def index():
    print 'hello'
    session['count'] += 1
    print session['count']
    return render_template('/index.html', count=session['count'])

@app.route('/add', methods=['POST'])
def add_count():
    session['count'] += 1
    return redirect('/')

@app.route('/reload', methods=['POST'])
def reload_page():
    session['count'] = 0
    return redirect('/')

app.run(debug=dev)
