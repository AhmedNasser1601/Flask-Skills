from flask import Flask, render_template

app = Flask(__name__)

my_skills = [("Python", 90), ("Java", 80), ("C++", 70), ("C#", 85), ("R", 50)]

@app.route("/")
def HomePage():
    return render_template(
        'HOME.html',
        title="H.O.M.E",
        welcome="Welcome to FLASK",
        custom_css="home",
        custom_js="home"
    )

if __name__ == "__main__":
    app.run(debug=True)
