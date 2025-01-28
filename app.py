from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///credits.db"
app.config["SQLALCHEMY_DATABASE_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class credits(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    credit = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}', '{self.credit}"

@app.route("/")
def hello_world():
    Credits = credits(name="NAME",credit="no of credits")
    db.session.add(Credits)
    db.session.commit()
    return render_template('index.html')

#return "<p>Hello, World!</p>"


@app.route("/p")
def p():
    return "<p>this is products page!</p>"

if __name__ == "__main__":
    app.run(debug=True)