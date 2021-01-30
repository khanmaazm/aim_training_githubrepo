import flask

app = flask.Flask(__name__)
app.config.from_object('config')

if app.config["RUNTYPE"] == 'PROD':
    runtype = 'PRODUCTION RUN'

@app.route('/', methods = ['GET'])
def home():    
   return "<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p1></body></html>"

@app.route('/firstpage')
def home():    
   return "<!DOCTYPE html><html><body><h1>First Page First</h1><p>My first paragraph.</p1></body></html>"

@app.route('/secondpage', methods = ['GET'])
def home():    
   return "<!DOCTYPE html><html><body><h1>My Second Page</h1><p>My second paragraph.</p1></body></html>"

@app.route('/thirdpage', methods = ['GET'])
def home():    
   return "<!DOCTYPE html><html><body><h1>My Third Page</h1><p>My third paragraph and explanation is finished.</p1></body></html>"

@app.route('/addormultiplenumbers', methods = ['POST'])
def addormul(request):
   arg1 = request.args['firstparam']
   resultout = arg1 + 4
   return resultout

#app.run()
#app.run(port=5001)
app.run('127.0.0.2')
#app.run('127.0.0.2', port = '9566')

