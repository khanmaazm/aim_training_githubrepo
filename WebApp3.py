import flask

app = flask.Flask(__name__)
@app.route('/', methods = ['GET'])
def home():    
   return "<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p1></body></html>"

@app.route('/second', methods = ['GET'])
def home():    
   return "Second Function Return"

app.run()
