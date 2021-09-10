from user_app import app
from flask import render_template, redirect, request
from user_app.models.user import User

@app.route("/")
def index():
    return render_template("create_user.html")

@app.route("/users_all")
def users_all():
    users_all = User.get_all()
    print(users_all)
    return render_template("users_all.html", users_all = users_all)

@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    new_user = User.create_user(data)
    return redirect("/users_all")

@app.route("/user_ind/<int:id>")
def user_ind(id):
    data = {
        "id" : id
    }
    user_ind = User.get_ind(data)
    print(user_ind)
    return render_template("user_ind.html", user = user_ind)

@app.route("/edit_user/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    print(request.method)
    if request.method == "POST":
        print(request.form)
        data = {
        "id" : id,
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
        }
        edited_user = User.edit_user(data)
        return redirect(f"/user_ind/{id}")
    else:
        user = User.get_ind({ "id" : id })
        return render_template("edit_user.html", user = user)


@app.route("/delete_user/<int:id>")
def delete_user(id):
    data = {
        "id" :  id
    }
    deleted_user = User.delete_user(data)
    return redirect("/users_all")