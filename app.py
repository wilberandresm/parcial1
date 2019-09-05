from flask import Flask,render_template,escape,request,jsonify

from flask import send_file,request     
from flask import make_response,send_file
import os
import time
import datetime
import pandas as pd

app=Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')    
def archivo(tiempo,temperatura,humedad,marca_tiempo):
    hora= time.localtime()
    horaT= time.strftime("%H:%M:%S", hora)
    print(horaT)
    datos=open("09052019.csv","a+")
    datos.write("\r\n"+horaT+", "+tiempo+", "+ tiempo+ ", "+ humedad+", "+marca_tiempo )
    datos.close()



@app.route('/log',methods= ['GET'])
def lista(): 
    try:
        temperatura=request.form.get('temperatura')
        humedad=request.form.get('humedad')
        tiempo=request.form.get('tiempo')
        marca_tiempo=datatime.now().strftime("%Y-%m-%d %H:%M:%S" )
        archivo(temperatura,humedad,tiempo,marca_tiempo)
    except:
        return render_template('formulario.html')

   


if __name__ == "__main__":
    app.run(debug= True, host= '0.0.0.0', port=80)
