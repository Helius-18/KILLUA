from flask import Flask,render_template,redirect,request
from flask.helpers import url_for
from flask.json import jsonify
import get_details
path="index.html"
epis={}
app=Flask(__name__)

@app.route("/templates/index.js")
def js():
    return render_template("index.js")

@app.route('/')
def projects():
    return render_template("index.html")

@app.route('/eng')
def eng():
    return render_template("eng.html")

@app.route('/get_movie/<path:subpath>', methods=['POST','GET'])
def killua(subpath):
    epis=jsonify(get_details.random_stuff("https://hdonlines.net/"+str(subpath)))
    epis.headers.add('Access-Control-Allow-Origin','*')
    return(epis)

@app.route('/movie')
def movie():
    return render_template("movie.html")

@app.route('/get_details<dname>',methods=['POST','GET'])
def get_detail(dname):
    jname=jsonify(get_details.killua(dname))
    jname.headers.add('Access-Control-Allow-Origin','*')
    return(jname)

@app.route('/get_episode/<path:subpath>', methods=['POST','GET'])
def get_movie(subpath):
    print("http://127.0.0.1:5000/get_episode/"+subpath)
    jname=jsonify(get_details.change_episode(subpath))
    jname.headers.add('Access-Control-Allow-Origin','*')
    return(jname)


if __name__=="__main__":
    print("starting python flash server")
    # import webbrowser
    # webbrowser.open("http://127.0.0.1:5000/")
    app.run(host='127.0.0.1',port=5000,debug=False)