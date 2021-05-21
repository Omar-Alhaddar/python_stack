from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html",row=8,col=8)

@app.route('/<x>')
def index4(x):

    return render_template("index.html",row=int(x),col=8)

@app.route("/<x>/<y>")
def play(x,y):

    return render_template("index.html",row=int(x),col=int(y))

@app.route("/<x>/<y>/<color1>/<color2>")
def colors(x,y,color1,color2):
    
    return render_template("index.html",row=int(x),col=int(y),color1=(color1),color2=(color2))

if __name__=="__main__":
    app.run(debug=True)