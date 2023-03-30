from flask import Flask, request

app = Flask(__name__) # dunder 

# decorator! 
@app.route("/", methods=["POST", "GET"])
def hello_world(): # hello world
	return "Hello world!"

@app.route("/other-route")
def other_response():
	return "This is another route!"

@app.route("/greeting/<name>")
def say_hello(name):
  return f"Hello {name.capitalize()}!"

@app.route("/song") # /song?name=Boys&artist=Lizzo
def say_song():
	name = request.args.get("name")
	artist = request.args.get("artist")
	return f"I really like {name} by {artist}!"

# @app.route("/hello/su")
# def hello_su():
# 	return "Hello Su!"


# flask --app server.py --debug
if __name__ == "__main__":
	app.run(debug=True, port=1234)

# Flask - micro web framework

# Django - a full-stack web framework

# FastAPI - "modern", "high-performance" web framework