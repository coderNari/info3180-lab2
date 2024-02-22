from app import app
from flask import render_template, request, redirect, url_for, flash
from datetime import datetime

###
# Routing for your application.
###
def format_date_joined(date_joined):
    date_obj = datetime.strptime(date_joined, '%Y-%m-%d')
    formatted_date = date_obj.strftime('%b, %Y')
    return formatted_date

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile')
def profile():
    """Render the website's profile page."""
    user_info = {
        'image_url': "{{url_for('static', filename=''app/static/ppic.jpg'')}}",
        'full_name': 'Narika Hall',
        'username': 'narihall',
        'location': 'Kingston, Jamaica',
        'join_date': '2021-02-21',  
        'bio': 'Tech Fanatic, Nature Lover and Car Enthusiast.',
        'posts_count': 10,
        'followers_count': 70,
        'following_count': 50,
    }

    # Format the join date using format_date_joined function
    formatted_join_date = format_date_joined(user_info['join_date'])

    user_info['formatted_join_date'] = formatted_join_date

    return render_template('profile.html', user=user_info)



###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
