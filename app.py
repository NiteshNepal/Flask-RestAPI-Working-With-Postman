# FLASK FRAMEWORK
"""
flask is a micro framework to designed for web developers, to enable them to create and scale web apps quickly and
simply.
Flask is nothing but a framework that holds some protocol and functions that provide some functionality to make an API.
we can establish a communication by the help of different API, and this Framework is provided by the help of Flask.
Flask is based in Python.

  Flask uses the following framework internally:
1.jinja---> It a internal framework that helps to call the necessary backend and run the output.
            for eg: If we click on a play button on youtube it is connected with certain backend to run the video,
            which allows us to play that video.

2.werkzeug---> It uses a internal protocol called as WSGI( Web server gateway Interface). It helps to call the
            necessary backend code and get the information.
"""
"""
SOAP- simple object access protocol- Old Protocol, mostly not in use nowadays.
REST- Representational State Transfer-it is a new protocol or architecture.

They are the structure by which we create these kind of API's.
we are going to follow REST.

"""
"""Postman is a popular software tool that allows developers to test, develop, and document
 APIs (Application Programming Interfaces). It provides a user-friendly graphical interface that
simplifies the process of sending requests to APIs and inspecting the responses.
Postman supports all popular HTTP methods such as GET, POST, PUT, DELETE, etc.
It allows you to add headers, URL parameters, and body content to your requests.
You can also save and organize your requests and responses in collections, which makes it easy to reuse them.
In addition to testing APIs, Postman also provides features for collaboration and documentation.
 You can share your collections with others, which makes it easy to collaborate on API development.
You can also generate documentation for your APIs, which can be useful for communicating with other developers or for
 creating API reference guides.
Overall,
 Postman is a powerful tool that can save developers time and simplify the process of developing and testing APIs."""
from flask import Flask, render_template, request, jsonify

# we can install all this required libraries at once by,
# first go to file and click on setting
# after reaching to the settings you will find the project you are working on
# click on that project and click on python interpreter and go to the top most bar which has add interpreter option.
# then click on conda environment, we can automatically add someof the libraries that is required in this project.


app = Flask(__name__)

#web application
@app.route('/', methods=['GET', 'POST'])  # To render Homepage
def home_page():
    return render_template('index.html')


@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method == 'POST'):  # it will only accept the post method not URL.
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if (operation == 'add'):
            r = num1 + num2
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html', result=result)


#postman
@app.route('/via_postman', methods=['POST'])  # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method == 'POST'):
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if (operation == 'add'):
            r = num1 + num2
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)


@app.route("/nitesh", methods=["POST"])  # will be called from postman with another route rename /nitesh
def sum():
    if (request.method == "POST"):
        num1 = int(request.json["num1"])
        num2 = int(request.json['num2'])
        result = num1 + num2
    return jsonify(result)

@app.route("/karma", methods=["POST"])
def info():
    if(request.method=="POST"):
        name=request.json["name"]
        email=request.json["mail"]
        address=request.json["Location"]
    return jsonify(name, email, address)


if __name__ == '__main__':
    app.run()
#main method is the superclass of all the classes present in the python.
# By this we can call all the constructor and any kind of object in the python.
