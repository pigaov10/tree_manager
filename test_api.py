from flask import url for 
from flask_base_tests_cases import TestFlaskBase

class TestTree(TestFlaskBase):
    def test_add_should_return_payload_without_id(self):
        data = {
            code: 'ABC',
            description: 'The new tree',
            age: 30
        }

        response = self.cliente.post(url_for('tree.add'), json=data)
        response.json.pop('id')
        self.assertEqual(data, response.json)