import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
	return '''
	<body>
	<h2>Hello World!</h2>
	</body>
	'''

@app.route("/greet/<name>")
def greet(name):
   return "Hello, %s" % name

if __name__ == '__main__':
   app.run(debug=True)

   ## DO NOT USE DEBUG MODE IN PRODUCTION!!!!!!!
   ## if there is a bug, all the debug info will be on the web
