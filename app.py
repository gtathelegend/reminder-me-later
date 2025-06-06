from flask import Flask, request, jsonify
from datetime import datetime
from models import db, Reminder

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/api/reminders/create', methods=['POST'])
def create_reminder():
    data = request.json

    required_fields = ['message', 'remind_at', 'method']
    if not all(field in data for field in required_fields):
        return jsonify({'success': False, 'error': 'Missing required fields'}), 400

    try:
        remind_at = datetime.fromisoformat(data['remind_at'])
    except ValueError:
        return jsonify({'success': False, 'error': 'Invalid datetime format'}), 400

    if data['method'] not in ['email', 'sms']:
        return jsonify({'success': False, 'error': 'Invalid method'}), 400

    reminder = Reminder(
        message=data['message'],
        remind_at=remind_at,
        method=data['method']
    )

    db.session.add(reminder)
    db.session.commit()

    return jsonify({
        'success': True,
        'data': {
            'id': reminder.id,
            'message': reminder.message,
            'remind_at': reminder.remind_at.isoformat(),
            'method': reminder.method
        }
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
