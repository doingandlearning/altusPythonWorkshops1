from flask import Flask, request, jsonify

app = Flask(__name__)

class Todo:
	def __init__(self, id, title, completed=False):
		self.id = id
		self.title = title
		self.completed = completed

	def to_dict(self):
		return {"id": self.id, "title": self.title, "completed": self.completed}

todos = [] # database, file system ... api call ... 

# Read the TODOs
# @app.route("/todos", methods=["GET"])
@app.get("/todos")
def get_todos():
	return jsonify([todo.to_dict() for todo in todos])


# C
# @app.route("/todos", methods=["POST"])
@app.post("/todos")
def create_todo():
	data = request.json
	id = len(todos) + 1 # Naive!! 
	title = data.get("title")

	if not title:
		return jsonify({"message": "You need to provide a todo title", "error": True}), 400
	
	todo = Todo(id, title)
	todos.append(todo)
	return jsonify(todo.to_dict()), 201


# U
@app.patch("/todos/<int:id>")
def update_todos(id):
	for todo in todos:
		if todo.id == id:
			data = request.json
			todo.title = data.get("title", todo.title)
			todo.completed = data.get("completed", todo.completed)
			return jsonify(todo.to_dict())
	return jsonify({"message": "Cannot find todo with given id", "error": True}), 404
# D
@app.delete("/todos/<int:id>")
def delete_todo(id):
	for todo in todos:
		if todo.id == id:
			todos.remove(todo)
			return "", 204	
	return jsonify({"message": "Cannot find todo with given id", "error": True}), 404

if __name__ == "__main__":
	app.run(debug=True)