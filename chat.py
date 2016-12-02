#!/bin/env python
from app import create_app, socketio

port = int(os.environ.get("PORT", 5000))
app = create_app(host='0.0.0.0', port=port)

if __name__ == '__main__':
    socketio.run(app)
