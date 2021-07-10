from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@dataclass
class ListItem(db.Model):
  id: int
  text: str
  done: bool

  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(200), nullable=False)
  done = db.Column(db.Boolean, default=False)

  def __repr__(self):
    return f'ListItem id={self.id}, text={self.text}, done={self.done}'
