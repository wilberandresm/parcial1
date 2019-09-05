from flask import Flask,render_template,escape,request,jsonify
from flask_sqlalchemy import SQLAlchemy  
from flask import send_file,request     
from flask import make_response,send_file
import os


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log',methods= ['GET'])
def lista(): 
    try:
        temperatura=request.args.GET('temperatura')
        humedad=request.args.GET('humedad')
        tiempo=request.args.GET('tiempo')
    except:
        return render_template('formulario.html')
@app.route('/log')
def return_file():
    return send_file('/Users/ceisutb07/Desktop/PageSoftware-master/archivo.csv',attachment_filename='archivo.csv')

@app.route('/log/',methods=['GET','POST'])
def file_downloads():
    if request.method == 'POST':
 # save the single "profile" file
        profile = request.files['profile']
        profile.save(os.path.join(uploads_dir, secure_filename(profile.filename)))
 # save each "charts" file
        for file in request.files.getlist('charts'):
            file.save(os.path.join(uploads_dir, secure_filename(file.name)))
        return redirect(url_for('localhost:80/log'))
    return render_template('fomrulario.html')
        
@app.route("/log")
def plot_csv():
    return send_file('outputs/Adjacency.csv',
                     mimetype='text/csv',
                     attachment_filename='Adjacency.csv',
                     as_attachment=True)

    
    

if __name__ == "__main__":
    app.run(debug= True, host= '0.0.0.0', port=80)
