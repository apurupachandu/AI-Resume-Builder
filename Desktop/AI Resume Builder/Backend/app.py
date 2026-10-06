from flask import Flask

app = Flask(_name_)


@app.route("/")
def home():
    return "AI Resume Builder - Project Started"


if _name_ == "_main_":
    app.run(debug=True)