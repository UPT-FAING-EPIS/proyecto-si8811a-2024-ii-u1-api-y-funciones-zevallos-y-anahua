# python -m unittest discover tests/

import unittest
from app import create_app, db
from app.models import Event

class EventApiTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.app_context():
            db.drop_all()

    def test_get_events(self):
        response = self.client.get('/events')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_event(self):
        response = self.client.post('/events', json={"name": "Nuevo Evento", "date": "2024-10-01"})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['name'], "Nuevo Evento")
        self.assertEqual(response.json['date'], "2024-10-01")

    def test_get_event(self):
        response = self.client.post('/events', json={"name": "Evento de Prueba", "date": "2024-10-01"})
        event_id = response.json['id']
        response = self.client.get(f'/events/{event_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], "Evento de Prueba")
        self.assertEqual(response.json['date'], "2024-10-01")

    def test_update_event(self):
        response = self.client.post('/events', json={"name": "Evento a Actualizar", "date": "2024-10-01"})
        event_id = response.json['id']
        response = self.client.put(f'/events/{event_id}', json={"name": "Evento Actualizado"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], "Evento Actualizado")
        self.assertEqual(response.json['date'], "2024-10-01")

    def test_delete_event(self):
        response = self.client.post('/events', json={"name": "Evento a Eliminar", "date": "2024-10-01"})
        event_id = response.json['id']
        response = self.client.delete(f'/events/{event_id}')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f'/events/{event_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
