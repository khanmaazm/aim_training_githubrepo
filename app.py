import flask
app = flask.Flask(__name__)
@app.route('/')
def home():
    return "<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p1></body></html>"

@app.route('/aws', methods = ['GET'])
def awshomepage():
    return "Second Function Return - This is AWS Home PAge"

@app.route('/azure', methods = ['GET'])
def azurehomepage():
    return "Second Function Return - This is Azure Home PAge"

app.run()