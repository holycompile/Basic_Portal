from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from connection import insert_user

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.php")

@app.route("/submit", methods=["POST"])
def submit():
    user_name= request.form["name"]
    user_address = request.form["address"]
    
    # Calling the seperate DB function
    insert_user(user_name, user_address)
    
    #finally the thankyou calling
    return redirect("/thankyou")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.php")

if __name__ == "__main__":
    app.run(debug=True)