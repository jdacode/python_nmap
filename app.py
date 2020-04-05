from flask import Flask, render_template, jsonify, json, make_response
from nmap import Nmap

app = Flask(__name__)


# Main Page Route
@app.route('/')
def index():
    return """<html><body>
  <h2>Hello Motherfuckers!</h2>
    <p>NMAP:</p>
    </body></html>""" + str(nmap1.run_nmap())


# Second Page Route
@app.route("/page2")
def page2():
  return """<html><body>
  <h2>Welcome to page 2</h2>
    <p>This is just amazing!</p>
    </body></html>"""


@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name

@app.route("/test")
def test():
    return nmap1.run_nmap()


@app.route('/summary')
def summary():
    d = nmap1.run_nmap()
    return make_response(jsonify(d), 200)



if __name__ == '__main__':
    nmap1 = Nmap('1.1.1.1')
    nmap1.run_nmap()
    app.run()



