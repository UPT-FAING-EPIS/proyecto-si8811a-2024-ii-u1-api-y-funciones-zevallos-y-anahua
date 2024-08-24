from flask import Blueprint, request, jsonify
from app import db
from app.models import Event

event_routes_blueprint = Blueprint('events', __name__)

@event_routes_blueprint.route('', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{'id': e.id, 'name': e.name, 'date': e.date} for e in events]), 200

@event_routes_blueprint.route('/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get(event_id)
    if event:
        return jsonify({'id': event.id, 'name': event.name, 'date': event.date}), 200
    else:
        return jsonify({"error": "Evento no encontrado"}), 404

@event_routes_blueprint.route('', methods=['POST'])
def create_event():
    data = request.get_json()
    if not data or 'name' not in data or 'date' not in data:
        return jsonify({"error": "Datos inválidos"}), 400

    new_event = Event(name=data['name'], date=data['date'])
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'id': new_event.id, 'name': new_event.name, 'date': new_event.date}), 201

@event_routes_blueprint.route('/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    event = Event.query.get(event_id)
    if not event:
        return jsonify({"error": "Evento no encontrado"}), 404

    if 'name' in data:
        event.name = data['name']
    if 'date' in data:
        event.date = data['date']
    
    db.session.commit()
    return jsonify({'id': event.id, 'name': event.name, 'date': event.date}), 200

@event_routes_blueprint.route('/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get(event_id)
    if event:
        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": "Evento eliminado"}), 200
    else:
        return jsonify({"error": "Evento no encontrado"}), 404
