from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def Login():
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def Register():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)