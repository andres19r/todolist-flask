from app import db
from datetime import datetime


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(128))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    completed = db.Column(db.DateTime, index=True)
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.name}>"

    def is_completed(self):
        return self.status

    def complete_task(self):
        if not self.is_completed():
            self.status = True
            self.completed = datetime.utcnow()


