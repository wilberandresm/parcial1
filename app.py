from flask import Flask,render_template,escape,request,jsonify
from flask_sqlalchemy import SQLAlchemy  
from flask import send_file,request     
from flask import make_response,send_file
import os
import time
import pandas as pd

app=Flask(__name__)

@app.route('/')
def index():

    tiempo_actual = time.strftime("%c")
    data = {'fecha':[tiempo_actual], 'tiempo': [2.22], 'temperatura': [22.7], 'humedad': [33.2]}
    df = pd.DataFrame(data, columns= ['fecha', 'tiempo', 'temperatura', 'humedad'])
    df.to_csv("09052019.csv")
    return render_template('index.html')    
    

@app.route('/log',methods= ['GET'])
def lista(): 
    try:
        temperatura=request.args.GET('temperatura')
        humedad=request.args.GET('humedad')
        tiempo=request.args.GET('tiempo')
    except:
        return render_template('formulario.html')

   


if __name__ == "__main__":
    app.run(debug= True, host= '0.0.0.0', port=80)
