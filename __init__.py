"""Import."""
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar,  View
from flask_bcrypt import Bcrypt
from forms import UserLogin, SignUp, ContactUs
from database import User, db 


def create_app():
    """Flask app."""
    app = Flask('blueprint')
    Bootstrap(app)
    app.config.from_pyfile('app.cfg')
    bcrypt = Bcrypt(app)

    @app.route("/")
    def _home():
        """Home."""
        return render_template('home.html')

    @app.route("/login", methods = ['GET', 'POST'])
    def _login():
        """Login."""
        form = UserLogin()
        if form.validate_on_submit():
            return "done."
        return render_template('login.html', form = form)

    @app.route("/logout")
    def _logout():
        """Logout."""
        return render_template('logout.html')

    @app.route("/signup", methods = ['GET', 'POST'])
    def _signup():
        """Signup."""
        form = SignUp()
        if form.validate_on_submit():
            return "done."
        return render_template('signup.html', form = form)

    @app.route("/contact", methods = ['GET', 'POST'])
    def _contact():
        """Contact."""
        form = ContactUs()
        if form.validate_on_submit():
            return "done"
        return render_template('contact.html', form = form)

    @app.route("/about")
    def _about():
        """About."""
        return render_template('about.html')

    return app
