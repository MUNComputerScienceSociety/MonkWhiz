from flask import Flask, render_template

###
# Everything you need to know to get started can be found in Flask's quickstart guide:
# http://flask.pocoo.org/docs/0.10/quickstart
###

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', name="user")


if __name__ == '__main__':
    app.run()
