'''

There is nothing called as UI here , its basic backend :)

So, stop judging and see the handcoded things :)

Thank you,

btw something might blow off too in the project too lazy to fix now

NVM............

Still proud no AI SLOP SHIT :)))
'''



from flask import Flask
from flask import render_template
from flask import request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'

db=SQLAlchemy(app)

# later for sqlite3
connect = sqlite3.connect('database2.db')

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50))
    amt=db.Column(db.Integer)
    

@app.route("/")
def home():
    return render_template ('index.html')

@app.route("/data_entry", methods=["GET","POST"])
def dataentry():
    if request.method=="POST":
        username=request.form.get("username")
        amt=request.form.get("amt")
        return redirect (url_for('data_entry_success', username=username , amt=amt ))
    return render_template('dataentry.html')
    
@app.route("/data_entry_success/<username>/<amt>")
def data_entry_success(username, amt):
    data=User(username=username, amt=amt)
    db.session.add(data)
    db.session.commit()
    return render_template("data_success.html",username=username, amt=amt)


@app.route("/all_data")
def full_data():
    all_data=User.query.all()
    return render_template("show_all_data.html", all_data=all_data)
    
    
    
    
@app.route('/delete_data', methods=["GET", "POST"])
def delete_data():
    if request.method=='POST':
        username=request.form.get("username")
        data= db.session.get(User,username)
        db.session.delete(data) 
        db.session.commit()
        return redirect(url_for('full_data'))
    return render_template("delete_data_form.html")
    
    
    
    
    
    

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)