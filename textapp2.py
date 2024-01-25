# Install required libraries
# pip install Flask Flask-SocketIO

from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# Store messages in memory (for demo purposes, not suitable for production)
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@socketio.on('message')
def handle_message(data):
    messages.append(data)
    socketio.emit('message', data, room=request.sid)  # Use room=request.sid for equivalent broadcast

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)


