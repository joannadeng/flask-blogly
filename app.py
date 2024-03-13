"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "i-am-secret-key"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.debug = True
debug = DebugToolbarExtension(app)


connect_db(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home_page():
    """list of users"""
    return redirect('/users')

@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template("list.html", users=users)

@app.route('/users/new')
def new_user_form():
    return render_template("new_user_form.html")

@app.route('/users/new', methods=["POST"])
def new_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_URL']

    user = User (first_name=first_name,last_name=last_name,image_url=image_url)
    db.session.add(user)
    db.session.commit()
    return redirect("/users")

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """show details about a single user"""
    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """edit a user"""
    user = User.query.get(user_id)
    return render_template("user_edit.html",user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def show_user_with_editing(user_id):
    """show details about a single user after editing"""
    user = User.query.get(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_URL = request.form['image_URL']
    db.session.add(user)
    db.session.commit()
    return redirect('/')

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    """delete a user"""
    User.query.filter_by(id=user_id).delete()
    db.session.commit()

    return redirect('/')

