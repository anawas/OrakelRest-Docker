from flask import Flask, jsonify, request, make_response, render_template
import jwt
from flask_sqlalchemy import SQLAlchemy
import datetime
from functools import wraps
from generators.generators import SpellGenerator, SymbolGenerator, NumberGenerator
from models.allowed_users import AllowedUsers

import logging

logging.basicConfig(filename="restapi.log", level=logging.INFO)

application = app = Flask(__name__)
app.config['SECRET_KEY'] = 'cccccckihedfgnrnvtirjenvhtkriienvddrnljfcue'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing. Please log in first'}), 401

        try:
            jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(*args, **kwargs)

    return decorated


@app.route('/')
def index():
    return render_template('index.html'), 200

@app.route('/orakel/spell')
@token_required
def get_spell():
    s = SpellGenerator()
    return jsonify({'spell': s.get_lucky_spell()})


@app.route('/orakel/number')
@token_required
def get_number():
    s = NumberGenerator()
    return jsonify({'number': s.get_lucky_number()})


@app.route('/orakel/symbol')
@token_required
def get_symbol():
    s = SymbolGenerator()
    return jsonify({'symbol': s.get_lucky_symbol()})


@app.route('/orakel/login')
def login():
    auth = request.authorization

    if not auth or not auth.password or not auth.username:
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})

    if auth and check_user(auth):
        token = jwt.encode({
            'user': auth.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('You need to login first!', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})


# Looks up the user in the database
def check_user(auth):
    # user = User.query.filter_by(username=auth.username).first()
    all_users = AllowedUsers()
    if all_users.is_allowed_user(auth.username, auth.password):
        logging.info(f"User {auth.username} logged in")
        return True
    logging.warning(f"Unauthorized logging attempt of user {auth.username}")
    return False


if __name__ == '__main__':
    logging.info("Starting server")
    app.run(host="0.0.0.0", port=80)
