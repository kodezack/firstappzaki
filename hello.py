from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
<<<<<<< HEAD
   return "Hello, World!"

if __name__ == '__main__':
    app.run(port=5000,debug=True)
=======
	return "Hello, World!"
#test
if __name__ == '__main__':
	app.run(port=5000,debug=True)
>>>>>>> 638a4ff03d6200a08bfa9362efe8e4252ecd64f9
