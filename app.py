from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/link')
def link():
    return render_template('link.html')

if __name__ == '__main__':
    app.run(debug=True)