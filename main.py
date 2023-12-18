# import flast module
from flask import Flask, request
import json

# instance of flask application
app = Flask(__name__)

todos = []

# home route that returns below text when root url is accessed
@app.route("/")
def home_page():
    with open("index.html", 'r') as file:
        html_content = file.read()
        return html_content


@app.route("/todo", methods=['POST'])
def create_todo():
    todo_name = request.form.get('todo')
    print(todo_name)
    id = len(todos) + 1
    todos.append({
        "id": id,
        "todo_name": todo_name
    })

    print(todos)
    return json.dumps({
        "success": True, 
        "id": id
    })


@app.route("/todo", methods=["GET"])
def get_all_todos():
    return json.dumps(todos)

@app.route("/todo", methods=["DELETE"])
def delete_todo(): 
    id = int(request.form.get("id"))
    new_todos = []
    for todo in todos: 
        if todo["id"] != id: 
            new_todos.append(todo)
    todos.clear()
    todos.extend(new_todos)
    return json.dumps({
        "success": True
    })

if __name__ == '__main__':
    app.run()
