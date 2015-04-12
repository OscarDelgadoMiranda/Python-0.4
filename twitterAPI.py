#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Oscar Delgado Miranda y Miguel Angel Perez Garcia'
import twitter
import io
import json


#Funcion para la conexion
def oauth_login():
    CONSUMER_KEY = '2TgBivZJndnZlQeuTgpm3m7oi'
    CONSUMER_SECRET = 'ta009qc3iUkH1fgZ0kwuGctqY4Ev3sQaVQc4bJ1swvA3wc18AV'
    OAUTH_TOKEN = '3159942879-LUIIk5ce2g9C4NbjJa8M9ZjV23hx9RUB6KJ6AHc'
    OAUTH_TOKEN_SECRET = '68PuK047NH2dM5FjFMqpeN8RUDVfkI6NfYTX8TapTjz8V'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api


#Funcion para grabar la informacion en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))


#Funcion para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()
	
