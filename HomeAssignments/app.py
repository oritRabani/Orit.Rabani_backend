from flask import Flask,  render_template, request, session, redirect, url_for
from interact_with_DB import interact_db
import json
import requests
app = Flask(__name__)
app.secret_key = '1234'
app.config.from_pyfile('settings.py')

# CV page - main page
@app.route('/')
def CV_page():
    return render_template('CV.html')

# CV contact form
@app.route('/CVcontact')
def CV_contact():
    return render_template('CVContactForm.html')

# assignment8 route to show the new html page created
@app.route('/assignment8')
def assign_8():
    userFound = True
    hobbiesFound = True
    if userFound and hobbiesFound:
        return render_template('assignment8.html', user= {'firstName': 'Orit', 'lastName': 'Rabani'},
                               hobbies = ('Skiing', 'Yoga', 'Shopping'))
    elif userFound and not hobbiesFound:
        return render_template('assignment8.html', user={'firstName': 'Orit', 'lastName': 'Rabani'})
    else:
        return render_template('assignment8.html')

@app.route('/thankYou')
def thanks():
    return render_template('thankYou.html')

# assignment 9 - forms
# dictionary of users
users = {'user1': {'name':'Orit', 'email': 'oritrab@post.bgu.ac.il', 'phoneNumber':'0526606415','gender': 'F'},
         'user2': {'name':'Nadav', 'email': 'Nadav@post.bgu.ac.il', 'phoneNumber':'0526606416','gender': 'M'},
         'user3': {'name':'Ruth', 'email': 'ruth@post.bgu.ac.il', 'phoneNumber':'0526606417','gender': 'F'},
         'user4': {'name':'Yuval', 'email': 'yuval@post.bgu.ac.il', 'phoneNumber':'0526606418','gender': 'M'},
         'user5': {'name':'Galya', 'email': 'Galya@post.bgu.ac.il', 'phoneNumber':'0526606419','gender': 'F'}}

@app.route('/logout')
def log_out():
    session['nick_name']=''
    return render_template('CV.html')

@app.route('/assignment9', methods=['GET','POST'])
def assign_9():
    if request.method == 'GET':
        if 'user_name' in request.args:
            user_name = request.args['user_name']
            if user_name == "":
                return render_template('assignment9.html', all_users = users)
            else:
                # email = request.args['email']
                # phone = request.args['phone']
                # gender = request.args['gender']
                for u_id, u_info in users.items():
                    if u_info['name'] == user_name:
                        email = u_info['email']
                        phone = u_info['phoneNumber']
                        gender = u_info['gender']
                        return render_template('assignment9.html', u_name = user_name, u_email = email, u_phone = phone, u_gender = gender)
        return render_template('assignment9.html')
    if request.method == 'POST':
        nick_name = request.form['nickName']
        password = request.form['password']
        #DB
        found = True
        if found:
            session['nick_name']= nick_name
            return redirect(url_for('CV_page'))
        else:
            return render_template('assignment9.html')


# Assignment 10 - Blueprint
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

# Return json format of users DB
@app.route('/assignment11/users')
def assign11_users_func():
    query = 'SELECT * FROM users'
    users = interact_db(query=query, query_type='fetch')
    json_users = json.dumps(users)
    return json_users

@app.route('/assignment11/outer_source',methods=['GET','POST'])
def assign11_outer_func():
    if request.method == 'GET':
        if 'id_backend' in request.args:
            number = int(request.args['id_backend'])
            wanted_user = get_wanted_user(number)
            return render_template('assignment11.html', wanted_user=wanted_user)
        return render_template('assignment11.html')
    if request.method == 'POST':
        return redirect(url_for('/assignment11/outer_source'))

def get_wanted_user(number):
    res = requests.get(f'https://reqres.in/api/users/{number}')
    res = res.json()
    return res

if __name__ == '__main__':
    app.debug = True
    app.run()
