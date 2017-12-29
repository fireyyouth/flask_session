#!/bin/python
from flask import Flask, session, request, redirect, url_for, render_template
import os
app = Flask(__name__)
users = {
    'frank':'frank',
    'han':'han'
}
values = {
    'frank':'hello',
    'han':'yeah'
}
@app.route('/')
def index():
    if session.get('username') in users:
        if request.args.get('value'):
            values[session['username']] =request.args.get('value')
        return render_template('index.html', value = values[session['username']])
    else:
        return redirect(url_for('login'))
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and users.get(request.form.get('uname')) == request.form.get('pwd'):
        session['username'] = request.form['uname']
        return redirect(url_for('index'))
    else:
        return '''
        <form method="post">
            <p>name<input name="uname"/></p>
            <p>password<input type="password" name="pwd"/></p>
            <input type="submit" value="login"/>
        </form>
        '''
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
app.secret_key = os.urandom(10)
app.run(debug=True)

