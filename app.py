from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TOTO JE MUJ WEB SERVER'

@app.route('/develop')
def test_stranka():
    return 'test stranka'

if __name__ == '__main__':
    app.run(debug=True)
