import json
from flask import Blueprint, current_app, request, jsonify
from models.tree import Tree 

bp_trees = Blueprint('trees', __name__)

@bp_trees.route('/list', methods=['GET'])
def list_all():
    cols = ['id', 'code', 'description', 'age']
    tree = Tree.query.all()
    result = [{col: getattr(d, col) for col in cols} for d in tree]
    return jsonify(result=result), 200

@bp_trees.route('/list/<id>', methods=['GET'])
def list_one(id):
    cols = ['id', 'code', 'description', 'age']
    tree = Tree.query.filter(Tree.id == id)
    #import ipdb; ipdb.set_trace();
    result = [{col: getattr(d, col) for col in cols} for d in tree]
    return jsonify(result=result), 200

@bp_trees.route('/modify/<id>', methods=['PUT'])
def update_one(id):
    Tree.query.filter(Tree.id == id).update()
    current_app.db.session.commit()
    return jsonify('It has been successfully modified'), 200

@bp_trees.route('/add', methods=['POST'])
def add_one():
    try:
        code = request.json['code']
    except:
        return 'Code is required', 422

    try:
        description = request.json['description']
    except:
        return 'Description is required', 422

    try:
        age = request.json['age']
    except:
        return 'Age is required', 422
    tree = Tree(code=code, description=description, age=age)
    current_app.db.session.add(tree)
    current_app.db.session.commit()
    return 'It has been successfully created', 201

@bp_trees.route('/delete/<id>', methods=['DELETE'])
def delete_one(id):
    Tree.query.filter(Tree.id == id).delete()
    current_app.db.session.commit()
    return jsonify('It has been successfully deleted'), 200