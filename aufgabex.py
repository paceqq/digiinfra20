import requests
import json

def jprint(obj):
	# Formatiert ein JSON Objekt in ein String Objekt und gibt dies aus
	text = json.dumps(obj, sort_keys=True, indent=4)
	print(text)

#Fügen Sie ihren Code unterhalb dieser Zeile ein

