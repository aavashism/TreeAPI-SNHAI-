import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
DATA_FILE = 'tree_data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_node(data, label, parent_id):
    new_id = max([node['id'] for node in flatten_tree(data)] + [0]) + 1
    new_node = {'id': new_id, 'label': label, 'children': []}
    if parent_id is None:
        data.append(new_node)
        return True
    parent = find_node_by_id(data, parent_id)
    if parent:
        parent['children'].append(new_node)
        return True
    return False

def find_node_by_id(nodes, node_id):
    for node in nodes:
        if node['id'] == node_id:
            return node
        child = find_node_by_id(node['children'], node_id)
        if child:
            return child
    return None

def flatten_tree(nodes):
    flat = []
    for node in nodes:
        flat.append({'id': node['id']})
        flat.extend(flatten_tree(node['children']))
    return flat

@app.route('/api/tree', methods=['GET'])
def get_tree():
    data = load_data()
    return jsonify(data)

@app.route('/api/tree', methods=['POST'])
def post_tree():
    req = request.get_json()
    label = req.get('label')
    parent_id = req.get('parentId')
    data = load_data()
    if add_node(data, label, parent_id):
        save_data(data)
        return jsonify({'status': 'success'}), 201
    return jsonify({'error': 'Parent not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
