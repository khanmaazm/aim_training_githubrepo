import flask
app = flask.Flask(__name__)
@app.route('/')
def home():
    return "Simple output"

@app.route('/aws', methods = ['GET'])
def awshomepage():
    return "Second Function Return - This is AWS Home PAge"

@app.route('/azure', methods = ['GET'])
def azurehomepage():
    return "Second Function Return - This is Azure Home PAge"
