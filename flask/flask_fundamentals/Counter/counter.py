from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    if 'count' in session:
        session['count'] = session['count'] + 1
    else:
        session['count'] = 1
    return render_template('counter.html')

@app.route('/addtwo')
def addtwo():
    session['count']+=1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)