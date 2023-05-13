from flask import Flask, request, jsonify, render_template

app=Flask(__name__)

@app.route("/Kshitiz")
def hello():
    test1=request.args.get("val1")
    test2=request.args.get("val2")
    test3=int(test1)+int(test2)
    return  '''<h1> my result is {} </h>''' .format(test3)
#the above is a get method which consist of URl+query
#if we want to run the above in browser then, http://127.0.0.1:5000/Kshitiz?val1=10&val2=10

@app.route("/kshitiz")
def hello1():
    return '''<h1> Hello Kshitiz </h1>'''

if __name__=="__main__":
    app.run()
