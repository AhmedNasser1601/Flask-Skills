from flask import Flask, render_template

app = Flask(__name__)

my_skills = [("Python", 90), ("Java", 80), ("C++", 70), ("C#", 85), ("R", 50)]

@app.route("/")
def HomePage():
    return render_template(
        'HOME.html',
        title="S.K.I.L.L.S",
        custom_css="home",
        page_head="My Skills",
        page_description="This is My Skills Page",
        skills=my_skills
    )

if __name__ == "__main__":
    app.run(debug=True)
