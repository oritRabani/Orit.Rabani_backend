from flask import Flask, redirect, url_for

app = Flask(__name__)

#homework 7 Orit Rabani

# regular route
@app.route('/welcome')
def welcome():
    return 'welcome to homework 7'

#redirect
@app.route('/home')
def home_page():
    return redirect('/welcome')

#regular route
@app.route('/aboutus')
def about_us():
    return 'orit rabani'

#redirect + url_for
@app.route('/products')
def products():
    return redirect(url_for('about_us'))


if __name__ == '__main__':
    app.run(debug=True)
