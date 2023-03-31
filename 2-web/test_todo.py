from todo import app
from unittest import  TestCase, main
import json

class TestTodo(TestCase):
	def setUp(self):
		self.app = app.test_client()
		self.todo = { "title": "This is a test todo" }

	def test_get_works(self):
		response = self.app.get("/todos")
		self.assertEqual(response.status_code, 200)

	
	def test_create_todo(self):
		response = self.app.post("/todos", data=json.dumps(self.todo), content_type="application/json")

		self.assertEqual(response.status_code, 201)
		
		data = response.get_json()
		
		self.assertEqual(data['title'], "This is a test todo")
		self.assertEqual(data['id'], 1)
		self.assertEqual(data['completed'], False)

if __name__ == "__main__":
	main()