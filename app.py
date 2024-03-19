from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/store/')
def store():
    return render_template('store.html')


@app.route('/clothing/')
def clothing():
    return render_template('clothing.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/jacket001/')
def jacket001():
    return render_template('jacket001.html')


if __name__ == '__main__':
    app.run()
