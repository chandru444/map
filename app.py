from flask import *
import pandas as pd
import sqlite3 as sql
import csv   
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/upload'

@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        name = request.form['username']
        id_no = request.form['id']
        con = sql.connect('map.db')
        cur = con.cursor()
        print(name)
        cur.execute('insert into Student(Name,Id_no) values(?,?)',(name,id_no))
        data = pd.read_sql_query('select * from student',con)
        print(data)
        con.commit()
        data.to_csv('student.csv',index=False)
        return redirect(url_for('homepage'))
    return render_template('student.html')
@app.route('/visitor',methods=['POST','GET'])
def visitor():
    if request.method == 'POST':
        name = request.form['username']
        mob = request.form['mob']
        con = sql.connect('map.db')
        cur = con.cursor()
        print(name)
        cur.execute('insert into Visitor(Name,Mobile) values(?,?)',(name,mob))
        data = pd.read_sql_query('select * from Visitor',con)
        print(data)
        con.commit()
        data.to_csv('visitor.csv',index=False)
        return redirect(url_for('homepage'))

    return render_template('visitor.html')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

if '__main__' == __name__:
    app.run(debug=True)

