from flask import Flask,  render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '1234'

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
users = {'user1': {'name':'Orit', 'email': 'oritrab@post.bgu.ac.il', 'phoneNumber':'0526606415'},
         'user2': {'name':'Nadav', 'email': 'Nadav@post.bgu.ac.il', 'phoneNumber':'0526606416'},
         'user3': {'name':'Ruth', 'email': 'ruth@post.bgu.ac.il', 'phoneNumber':'0526606417'},
         'user4': {'name':'Yuval', 'email': 'yuval@post.bgu.ac.il', 'phoneNumber':'0526606418'},
         'user5': {'name':'Galya', 'email': 'Galya@post.bgu.ac.il', 'phoneNumber':'0526606419'}}

@app.route('/logout')
def log_out():
    session['nick_name']=''
    return render_template('CV.html')

@app.route('/assignment9', methods=['GET','POST'])
def assign_9():
    if request.method == 'GET':
        if 'user_name' in request.args:
            user_name = request.args['user_name']
            email = request.args['email']
            phone = request.args['phone']
            gender = request.args['gender']

            if user_name == "":
                return render_template('assignment9.html', all_users = users)
            else:
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

if __name__ == '__main__':
    app.run()
