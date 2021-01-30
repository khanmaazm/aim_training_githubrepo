import flask

app = flask.Flask(__name__)
@app.route('/', methods = ['GET'])
def home():    
   return "Default Home Function Return"

@app.route('/second', methods = ['GET'])
def home():    
   return "Second Function Return"

app.run()
