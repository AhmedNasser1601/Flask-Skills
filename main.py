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

@app.route("/skills")
def SkillsPage():
    return render_template(
        "SKILLS.html",
        title="S.K.I.L.L.S",
        custom_css="skills",
        custom_js="skills",
        page_head="My Skills",
        page_description="This is My Skills Page",
        skills=my_skills
    )

@app.route("/add")
def AddPage():
    return render_template(
        "ADD.html",
        title="A.D.D",
        custom_css="add",
        custom_js="add"
    )

@app.route("/about")
def AboutPage():
    return render_template(
        "ABOUT.html",
        title="A.B.O.U.T",
        custom_css="about",
        custom_js="about"
    )

if __name__ == "__main__":
    app.run(debug=True)
