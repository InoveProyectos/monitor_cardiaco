#!/usr/bin/env python
'''
Monitor cardíaco
---------------------------
Autor: Inove Coding School
Version: 1.0
 
Descripcion:
Se utiliza Flask para crear un WebServer que levanta los datos de alquileres de inmuebles
y los presenta en un mapa distribuidos por ubicación
 
Ejecución: Lanzar el programa y abrir en un navegador la siguiente dirección URL
http://127.0.0.1:5000/

Nos deberá aparecer el mapa con los alquileres de la zona, identificados por color:
- Verde: Alquiler dentro del promedio en precio
- Amarillo: Alquiler debajo del promedio en precio
- Rojo: Alquiler por arribba del promedio en precio
- Azul: Alquiler en dolares US$

- Podremos también visualizar el análisis de los alquileres de la zona
http://127.0.0.1:5000/reporte

- Podremos visualizar la predicción de costo de alquiler basado
 en el algoritmo de inteligencia artificial implementado
http://127.0.0.1:5000/prediccion

Requisitos de instalacion:

- Python 3.x
- Libreriras (incluye los comandos de instalacion)
    pip install numpy
    pip install pandas
    pip install -U Flask
'''

__author__ = "Inove Coding School"
__email__ = "INFO@INOVE.COM.AR"
__version__ = "1.0"


import traceback
import io
import sys
import os


import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template, Response, redirect
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Indico la carpeta en donde se encuentran los templates html
APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, 'monitor_cardiaco')
TEMPLATE_PATH = os.path.join(APP_PATH, 'templates')
TEMPLATE_PATH = os.path.join(TEMPLATE_PATH, 'monitor')

app = Flask(__name__, template_folder='./templates/monitor')

@app.route("/")
def index():
    return redirect('/monitor')

@app.route("/monitor")
def monitor():
    return render_template('index.html')

@app.route('/monitor/registro')
def registro():
    try:
        nombre = request.args.get('nombre')
        if nombre is None:
            nombre = 'Pedro'

        df = pd.read_csv("propiedades.csv")

        result = df.to_json()
        return(result)
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route('/monitor/tabla')
def tabla():
    try:
        df = pd.read_csv("tabla.csv")
        result = df.to_json()
        return(result)
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route('/monitor/reporte')
def reporte():
    try:
        # Genero el reporte del usuario solicitado

        fig, ax = plt.subplots(figsize = (16,9))        
        img=mpimg.imread('deteccion_estres.png')
        ax.imshow(img)
        ax.set_title('Detector de estrés con inteligencia artificial')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
       
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')
    except:
        return jsonify({'trace': traceback.format_exc()})


if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line argument
    except:
        port = 5000 # Puerto default
        
    app.run(host='0.0.0.0', port=port, debug=True)
