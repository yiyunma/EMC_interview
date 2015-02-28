#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Welcome'
	
@app.route('/data', methods=['GET'])
def data():
	if request.method == 'GET':
		n = request.args.get('n')
		print "input number is %d" % n
	return "GET\n"

@app.route('/fib')
def fib(n):
	if n < 0:
		raise ValueError("n should not be a negative number")
	else:
		a = 0
		b = 1
		for i in range(0, n):
			temp = a
			a = b
			b = temp + b
			print a
		return "End"

if __name__ == '__main__':
	app.run(debug=True)
