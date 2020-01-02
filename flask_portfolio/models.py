from flask_portfolio import db

class Example(db.Model)
    id = db.column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    date_started = db.Column(db.String(11), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=True, nullable=False)
    github_link = db.Colummn(db.String(200), unique=True, nullable=True)
    live_link = db.Column(db.String(200), unique=True, nullable=True)

    def __repr__(self):
        return f"Example('{self.title}', '{self.date_started}', '{self.description}', '{self.github_link}', '{self.live_link}')"
