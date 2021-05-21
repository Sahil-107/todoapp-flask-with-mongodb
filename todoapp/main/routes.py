from flask import Blueprint, render_template, redirect, url_for, request
from bson.objectid import ObjectId

from todoapp.extensions import mongo
main = Blueprint('main',__name__)

@main.route('/')
def index():
    todos_collection = mongo.db.todos_collection
    todos = todos_collection.find()
    return render_template('index.html', todos=todos)

@main.route('/add_todo', methods=['POST'])
def add_todo():
    todos_collection = mongo.db.todos_collection
    todo_item = request.form.get('add-todo')
    todos_collection.insert_one({'text':todo_item, 'complete': False})
    return redirect(url_for('main.index'))

@main.route('/complete_todo/<oid>')
def complete_todo(oid):
    todo_collection = mongo.db.todos_collection
    todo_item = todo_collection.find_one({'_id': ObjectId(oid)})
    todo_item['complete']=True
    todo_collection.save(todo_item)
    return redirect(url_for('main.index'))

@main.route('/delete_completed')
def delete_completed():
    todo_collection = mongo.db.todos_collection
    todo_collection.delete_many({'complete':True})
    return redirect(url_for('main.index'))

@main.route('/delete_all')
def delete_all():
    todo_collection = mongo.db.todos_collection
    todo_collection.delete_many({})
    return redirect(url_for('main.index'))