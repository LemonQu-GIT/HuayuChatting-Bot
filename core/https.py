from flask import Flask
from weekchart import paint
from flask import send_file
from flask import render_template
import os

app=Flask(__name__)

@app.route('/favicon.ico')
def get_fav():
    return send_file('../favicon.ico')

@app.route('/weekchart/<schoolID>',methods = ['POST','GET'])
def weekchart(schoolID):
    os.system("python weekchart.py --id "+schoolID)
    return send_file('../out/weekchart.png', mimetype='image/png')

@app.route('/weekpie/<time>',methods = ['POST','GET'])
def weekpie(time):
    os.system("python weekpie.py --time "+time)
    return send_file('../out/weekpie.png', mimetype='image/png')

@app.route('/weektable')
def index():
    # os.system("python weektable.py")
    # os.system("python xls2pdf.py")
    return send_file('./华育校友营周发言比率.pdf')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
   app.run(debug = True)