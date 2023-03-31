import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = 'some super secret key!'
socketio = SocketIO(app, logger=True)


@app.get("/")
def get_home_page():
	emit("error_message", {'message': "Important error message"}, broadcast=True)
	# emit('message', {'text': data['text'], 'user': data['user']}, broadcast=True)
	return render_template("index.html", date = datetime.datetime.now())

@app.get("/chat/<username>")
def get_chat_page(username):
	return render_template("chat.html", username=username)

@socketio.on("send_message")
def message_received(data):
	emit('message', {'text': data['text'], 'user': data['user']}, broadcast=True)

if __name__ == "__main__":
	# app.run(debug=True)
	socketio.run(app, port=5000, debug=True)