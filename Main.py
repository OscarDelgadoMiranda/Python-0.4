#!/usr/bin/python
# -*- coding: utf-8 -*-

#Grupo 13:
#Oscar Delgado Miranda
#Miguel Angel Perez Garcia

from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
from pprint import pprint

app = Flask(__name__)
GoogleMaps(app)

import twitterAPI
import json

#Conexion
twitter_api =  twitterAPI.oauth_login()

print "Buscando tweets que contengan 'Cadiz 2015'..."

#Buscamos los tweets que contengan "Cadiz 2015", desde las coordenadas de Cadiz capital, en un radio de 500km y como maximo 100 tweets
search_results = twitter_api.search.tweets(q="Cadiz 2015", geocode='36.516380894202264,-6.282446299999947,500km',count=100)

#Los guardamos en un fichero
twitterAPI.save_json("trends",search_results) 

#Leemos del fichero los tweets
with open('trends.json') as data_file:
	data = json.load(data_file)

#Creamos una lista con las coordenadas de los tweets
lista_coordenadas = []
for estado in data["statuses"]:
	if estado["coordinates"]!= None:
		coordenadas = estado["coordinates"]
		xy=[coordenadas.values()[1][1] , coordenadas.values()[1][0]]
		lista_coordenadas.append(xy)

#Impresion de las coordenadas de los tweets
print "Coordenadas de los tweets: "
pprint(lista_coordenadas)

#Creacion del mapa
@app.route("/")
def mapview():
	mymap = Map(
		identifier="view-side",
		lat=36.516380894202264,
		lng=-6.282446299999947,
		markers=lista_coordenadas,
		style="height:800px;width:800px;margin:0;" 
	)
	return render_template('mapa.html', mymap=mymap)

if __name__ == "__main__":
	app.run()
