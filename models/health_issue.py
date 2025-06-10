from database.db import db

class HealthIssue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    diagnosed_by = db.Column(db.String(100))  # Médecin ou source
    date_diagnosed = db.Column(db.Date)
