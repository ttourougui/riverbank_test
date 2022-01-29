# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    import os
    ENV = os.getenv('ENV')
    return f'Hey, we have Flask in {ENV}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')