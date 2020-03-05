from flask import request, redirect, url_for, render_template, flash, abort, jsonify
from HISEN import app, db
from HISEN.models import ResultIkka,Ikka,seed
from HISEN import Nijushisekki
from HISEN import Kannshi
from HISEN import Kyokusuu



@app.route('/', methods = ["GET" , "POST"])
def form():
    return render_template('form.html')

@app.route('/result', methods = ["GET" , "POST"])
def result():
   if request.method == 'POST':
       year = int(request.form['year'])
       month = int(request.form['month'])
       day = int(request.form['day'])


       sekki = Nijushisekki.nijushisekki(month * 2 -1,year)
       julian_day = Kannshi.Julian_Day(year,month,day)
       jikkann_year = Kannshi.jikkann_year(year,month,day)
       juunishi_year = Kannshi.juunishi_year(year,month,day)
       gessho_index = Kannshi.gessho(sekki,month,day)
       jikkann_day =  Kannshi.jikkann_day(julian_day)
       juunishi_day = Kannshi.juunishi_day(julian_day)

       kanshi_year = Kannshi.get_jikkann(jikkann_year) + Kannshi.get_juunishi(juunishi_year)
       gessho = Kannshi.get_juunishi(gessho_index)
       kanshi_day = Kannshi.get_jikkann(jikkann_day) + Kannshi.get_juunishi(juunishi_day)
       kyoku = Kyokusuu.kyoku(juunishi_year,gessho_index)
       tyuya = Kyokusuu.tyuya(gessho_index)
       result = ResultIkka.query.filter(ResultIkka.kanshi_day == kanshi_day,ResultIkka.kyoku == kyoku,ResultIkka.tyuya == tyuya).first()
       juunitensho = result.juunitensho
       text = Ikka.query.filter(Ikka.juunitensho == juunitensho).first().text
       return render_template('result.html',kanshi_year = kanshi_year,gessho = gessho,kanshi_day = kanshi_day,kyoku = kyoku,tyuya = tyuya,juunitensho = juunitensho,text = text)
   else:
       return render_template('result.html')

@app.route('/edit', methods = ["GET" , "POST"])
def edit():
    if request.method == 'POST':
        ikka = Ikka.query.filter(Ikka.juunitensho == request.form['juunitensho']).first()
        if ikka is None:
            ikka = Ikka(juunitensho = request.form['juunitensho'],
                        text = request.form['text'])
            db.session.add(ikka)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            ikka.text = request.form['text']
            db.session.add(ikka)
            db.session.commit()
            return redirect(url_for('index'))

    else:
        resultikka = ResultIkka.query.get(1)
        if resultikka  is None:
            seed()
    return render_template('edit.html')


@app.route('/index', methods = ["GET" , "POST"])
def index():
    ikka = Ikka.query.all()
    return render_template('index.html',Ikka = ikka)



#print(julian_day)
#print("年干支：" + kanshi_year)
#print("月将：" + gessho)
#print("日干支：" + kanshi_day)
#print(kyoku + "局")
#print(tyuya)
