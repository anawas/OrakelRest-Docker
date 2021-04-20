import logging
from flask import Flask, jsonify, render_template
from generators.generators import SpellGenerator, SymbolGenerator, NumberGenerator

# Es ist eine gute Idee, die Zugriffe auf das API zu loggen
logging.basicConfig(filename="restapi.log", level=logging.INFO)

application = app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html'), 200


@app.route('/orakel/spell')
def get_spell():
    s = SpellGenerator()
    return jsonify({'spell': s.get_lucky_spell()})


@app.route('/orakel/number')
def get_number():
    s = NumberGenerator()
    return jsonify({'number': s.get_lucky_number()})


@app.route('/orakel/symbol')
def get_symbol():
    s = SymbolGenerator()
    return jsonify({'symbol': s.get_lucky_symbol()})


if __name__ == '__main__':
    logging.info("Starting server")
    app.run(host="0.0.0.0", port=80)
