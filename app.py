from flask import Flask

app = Flask(__name__)

@app.route('/')
def fun():
    return 'hello world'

@app.route('/nothing')
def nothing():
    return 'nothing here'


if __name__ == "__main__":
    app.run(debug=True)

