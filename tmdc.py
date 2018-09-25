from app import app

app.config['SECRET_KEY']

import os

port = int(os.getenv('PORT', 8000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
