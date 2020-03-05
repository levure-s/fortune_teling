from HISEN import db
from HISEN import seedResultIkka

class ResultIkka(db.Model):
    __tablename__ = 'resultikka'
    id = db.Column(db.Integer, primary_key=True)
    kanshi_day = db.Column(db.String)
    kyoku = db.Column(db.String)
    tyuya = db.Column(db.String)
    juunitensho = db.Column(db.String)

    def __repr__(self):
        return '<ResultIkka id={id} kanshi_day={kanshi_day!r}>'.format(
                id=self.id, kanshi_day=self.kanshi_day)

class Ikka(db.Model):
    __tablename__ = 'ikka'
    id = db.Column(db.Integer, primary_key=True)
    juunitensho = db.Column(db.String)
    text = db.Column(db.Text)

    def __repr__(self):
        return '<Ikka id={id} juunitensho={juunitensho!r}>'.format(
                id=self.id, juunitensho=self.juunitensho)

def init():
    db.create_all()

def seed():
    for result in seedResultIkka.results:
        resultikka = ResultIkka(kanshi_day = result[0],kyoku = result[1],tyuya  = result[2],juunitensho = result[3])
        db.session.add(resultikka)
        db.session.commit()
