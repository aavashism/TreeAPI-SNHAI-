import unittest
import json
from app import app, save_data

class TreeApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        initial_data = [{
            "id": 1,
            "label": "root",
            "children": []
        }]
        save_data(initial_data)

    def test_get_tree(self):
        response = self.app.get('/api/tree')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data[0]['label'], 'root')

    def test_post_tree_valid(self):
        response = self.app.post('/api/tree', json={
            "label": "child1",
            "parentId": 1
        })
        self.assertEqual(response.status_code, 201)
        tree = json.loads(self.app.get('/api/tree').data)
        self.assertEqual(tree[0]['children'][0]['label'], "child1")

    def test_post_tree_invalid_parent(self):
        response = self.app.post('/api/tree', json={
            "label": "orphan",
            "parentId": 999
        })
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()
