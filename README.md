<h1 align=center>Flask Skills</h1>
This is a simple Flask application that demonstrates how to create a basic website with multiple pages, each with its own custom CSS and JavaScript files. The app also includes a skills page that displays a list of skills and their proficiency levels.

## Deployed on Microsoft Azure:
> ### Go to: <a href="http://flask-skills.azurewebsites.net/">http://flask-skills.azurewebsites.net</a>

## Prerequisites
To run this app, you will need the following:
* Python 3.6 or later
* Flask
* Jinja2
* A text editor

## Installation
1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Run the app.
    - <code>git clone https://github.com/ahmednasser1601/flask-skills.git</code>
    - <code>cd flask-skills-app</code>
    - <code>pip install -r requirements.txt</code>
    - <code>flask run</code>

## Usage
The app has four pages:
* Home page
* Skills page
* Add page
* About page

To navigate between pages, click on the links in the navigation bar.

## Code Explanation
The app consists of the following files:
* `main.py`: The main Flask app file.
* `static/css/master.css`: The main CSS file for the app.
* `static/js/master.js`: The main JavaScript file for the app.
* `templates/base.html`: The base HTML template for all pages.
* `templates/home.html`: The HTML template for the home page.
* `templates/skills.html`: The HTML template for the skills page.
* `templates/add.html`: The HTML template for the add page.
* `templates/about.html`: The HTML template for the about page.

The `main.py` file is the main entry point for the app. It creates a Flask app and defines the routes for each page. The `static/css/master.css` file contains the main CSS styles for the app. The `static/js/master.js` file contains the main JavaScript code for the app.

The `templates/base.html` file is the base HTML template for all pages. It includes the basic HTML structure and the navigation bar. The `templates/home.html`, `templates/skills.html`, `templates/add.html`, and `templates/about.html` files are the HTML templates for each page. They extend the `templates/base.html` file and add the specific content for each page.
