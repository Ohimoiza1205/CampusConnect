<<<<<<< HEAD
# This is where we define utility functions for authentication
=======
from functools import wraps
from flask import session, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function
>>>>>>> e86c179ae670f259e3f9485453cc6bd9771385c7
