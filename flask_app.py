from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("index.html")

@app.route('/resources', methods=['GET'])
def mains():
    # found in ../templates/
    return render_template("resources.html")

@app.route('/help', methods=['GET'])
def mainss():
    # found in ../templates/
    return render_template("help.html")

@app.route('/r1', methods=['GET'])
def mainsss():
    # found in ../templates/
    return render_template("resource_1.html")

@app.route('/r2', methods=['GET'])
def min():
    # found in ../templates/
    return render_template("resource_2.html")

@app.route('/r3', methods=['GET'])
def minss():
    # found in ../templates/
    return render_template("resource_3.html")

@app.route('/r4', methods=['GET'])
def minsss():
    # found in ../templates/
    return render_template("resource_4.html")

@app.route('/r5', methods=['GET'])
def minssss():
    # found in ../templates/
    return render_template("resource_5.html")

@app.route('/r6', methods=['GET'])
def minsssss():
    # found in ../templates/
    return render_template("resource_6.html")

@app.route('/h1', methods=['GET'])
def load():
    # found in ../templates/
    return render_template("help_1.html")

@app.route('/h2', methods=['GET'])
def loadd():
    # found in ../templates/
    return render_template("help_2.html")

@app.route('/h3', methods=['GET'])
def loads():
    # found in ../templates/
    return render_template("help_3.html")

@app.route('/h4', methods=['GET'])
def loadss():
    # found in ../templates/
    return render_template("help_4.html")

@app.route('/h5', methods=['GET'])
def looad():
    # found in ../templates/
    return render_template("help_5.html")

@app.route('/h6', methods=['GET'])
def loaad():
    # found in ../templates/
    return render_template("help_6.html")
