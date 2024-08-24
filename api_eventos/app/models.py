from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Event {self.name}>'
