from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route('/')
@app.route('/index')
def start_here():
    """Home page."""

    return render_template('index.html')


@app.route('/application-form')
def display_application_form():
    """Show the application form."""

    return render_template('application-form.html')


@app.route('/application-success')
def display_applicaton_form_response():
    """Displays the application form response."""

    return render_template('application-response.html')


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
