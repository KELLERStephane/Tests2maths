#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob, os, sys
from datetime import datetime
from sys import version

#Fonction qui renvoie la température
def get_temp(device_file):
    temp_c = 0

    if os.path.isfile(device_file):
	# ouverture du fichier en mode read 'r' (lecture en mode texte)
	with open(device_file,'r') as fichier:
		lines = fichier.readlines()

        if lines[0].strip()[-3:] == 'YES':
            equals_pos = lines[1].find('t=')

            if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0

    return temp_c

#Dossier du dispositif DS18B20
base_dir = '/sys/bus/w1/devices/'
devices_folder = glob.glob(base_dir + '28*')

#Récupération de l'id du capteur
for device_dir in devices_folder:
    device = os.path.basename(device_dir)


    temp = round(get_temp(device_dir+'/w1_slave'), 1)

#Affichage de la température selon la version de python
message = 'Température : '+str(temp) + '°C'
if version[0] == '2':
	print "id capteur :", device
	print message
else:
	print("id capteur :", device)
	print(message)

