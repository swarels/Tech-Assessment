from flask_sqlalchemy import SQLAlchemy
from app import db

class Shift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Shift {self.employee} from {self.start_time} to {self.end_time}>'
