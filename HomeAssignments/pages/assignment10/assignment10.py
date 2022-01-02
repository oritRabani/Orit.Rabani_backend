from flask import Blueprint, render_template, request, session, redirect, url_for
from interact_with_DB import interact_db

# assignment10 blueprint definition
assignment10 = Blueprint('assignment10', __name__, static_folder='static',
                         static_url_path='/assignment10', template_folder='templates')


# Routes
@assignment10.route('/assignment10')
def assignment10_func():
    query = 'select * from users'
    users = interact_db(query=query,query_type='fetch')
    return render_template('assignment10.html', users= users)

@assignment10.route('/insert_user', methods=['POST'])
def insert_func():
    # get the data from the form
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    gender = request.form['gender']

    # Insert to DB
    query = 'INSERT INTO users(name ,email,password,phoneNumber, gender) VALUES ("%s","%s","%s","%s","%s");' % (name, email, password, phone, gender)
    interact_db(query=query,query_type='commit')

    # come back to page
    return redirect('/assignment10')


@assignment10.route('/update_user',methods=['POST'])
def update_func():
    # get the data from the form
    old_email = request.form['OldEmail']
    new_email = request.form['NewEmail']
    old_phone = request.form['OldPhone']
    new_phone = request.form['NewPhone']

    # Insert to DB
    query = 'UPDATE users SET email = "%s" WHERE email = "%s";' % (new_email, old_email)
    interact_db(query=query, query_type='commit')

    query2 = 'UPDATE users SET phoneNumber = "%s" WHERE phoneNumber = "%s";' % (new_phone, old_phone)
    interact_db(query=query2, query_type='commit')
    # come back to page
    return redirect('/assignment10')

@assignment10.route('/delete_user',methods=['POST'])
def delete_func():
    user_id = request.form['id']
    query = 'Delete from users where id ="%s";' % user_id
    interact_db(query=query, query_type='commit')

    return redirect('/assignment10')

