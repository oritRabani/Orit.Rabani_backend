from flask import Flask,  render_template

app = Flask(__name__)

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
if __name__ == '__main__':
    app.run()
