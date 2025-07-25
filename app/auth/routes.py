from flask import Blueprint, render_template, redirect, url_for, session, flash
from authlib.integrations.flask_client import OAuth
from app.database.user import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard.dashboard'))
    return render_template('login.html')

@auth_bp.route('/login')
def login():
    # OAuth login logic here
    pass

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.index'))