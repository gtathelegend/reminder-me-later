from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    remind_at = db.Column(db.DateTime, nullable=False)
    method = db.Column(db.String(10), nullable=False)  # 'email' or 'sms'
    created_at = db.Column(db.DateTime, server_default=db.func.now())
