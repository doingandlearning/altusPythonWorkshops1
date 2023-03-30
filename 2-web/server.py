from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__) # dunder 

# decorator! 
@app.route("/", methods=["POST", "GET"])
def hello_world(): # hello world
	return jsonify({"message":"Hello world!"})

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

@app.route("/divide")
def divide():
	a = int(request.args.get("a"))
	b = int(request.args.get("b"))

	# if(b == 0):
	# 	return "This ain't Math", 400
	try:
		return f"{a/b}"
	except ZeroDivisionError:
		return "This ain't maths", 400
	except Exception as error:
		print(error) # telemetry, logging system!!
		return "There was an error", 400
# @app.route("/hello/su")
# def hello_su():
# 	return "Hello Su!"

@app.route('/days_until')
def days_until():
    date_str = request.args.get('date')
    try:
        target_date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return 'Invalid date format, use YYYY-MM-DD.'

    today = datetime.now().date()
    
    if target_date.date() < today:
        return 'The given date is in the past.'
    
    days_left = (target_date.date() - today).days
    print(date_str)
    
    return f"{days_left} days left."

# flask --app server.py --debug
if __name__ == "__main__":
	app.run(debug=True, port=1234)

# Flask - micro web framework

# Django - a full-stack web framework

# FastAPI - "modern", "high-performance" web framework