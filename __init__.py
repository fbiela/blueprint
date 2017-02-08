"""Import."""
from flask import Flask, render_template, redirect, url_for


def create_app():
    """Flask app."""
    app = Flask('blueprint')
    app.config.from_pyfile('app.cfg')

    @app.route("/")
    def _home():
        """Home."""
        return render_template('home.html')

    @app.route("/login")
    def _login():
        """Login."""
        return render_template('login.html')

    @app.route("/logout")
    def _logout():
        """Logout."""
        return render_template('logout.html')

    @app.route("/signup")
    def _signup():
        """Signup."""
        return render_template('signup.html')

    app.route("/contact")
    def _contact():
        """Contact."""
        return render_tempate('contact.html')

    app.route("/about")
    def _about():
        """About."""
        return render_template('about.html')

    return app
