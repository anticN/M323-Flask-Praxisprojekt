import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"

@app.route('/a1g/<int:x>/<int:y>')
def pure_function(x,y):
    return str(x+y)


if __name__ == '__main__':
    app.run(debug=True)
