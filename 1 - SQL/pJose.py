# -*- coding: utf-8 -*-

import MySQLdb


Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)

# Insertamos algunos registros (de forma cutre e ineficiente) para tener con qué trabajar
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (1, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (2, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (3, \"Bestia del Pantano\",\"Monstruo\",\"Destripado\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (4, \"Serpiente\",\"Monstruo\",\"Destripado\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (5, \"Scerdote maligno\",\"Monstruo\",\"Desmembramiento a espada\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (6, \"Bruja\",\"Recopiladora de hechizos\",\"Maldicion\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (7, \"Hombre lobo\",\"Monstruo\",\"Bala de plata\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (8, \"Caballero zombie\",\"Muerto viviente\",\"Destripado\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (9, \"Hombre Serpiente\",\"Monstruo\",\"Destripado\");"
micursor.execute(query)
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (10, \"Scerdote maligno\",\"Monstruo\",\"Quemado\");"
micursor.execute(query)

correcto = False
lastID = 10
insertar = True
while insertar:

	nombre = raw_input ('Inserte nombre del elemento \n')
	profesion = raw_input ('Inserte el campo profesion \n ')
	muerte = raw_input ('Inserte el campo muerte \n')

	if  (nombre  is not '') and (muerte  is not '') and (profesion is not ''):
		query = "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (" + str(lastID+1) + ",'" + nombre + "','" + profesion +"','" + muerte + "');"
		micursor.execute(query)
		lastID = lastID + 1
		correcto = True 
	else: 
		print ' \n\n Fallo introducioendo los datos! \n\n'

	posibles = ['n','N','y','Y','']
	segirIns = 'x'
	
	while segirIns not in posibles:
		
		segirIns = raw_input('Segir insertando Y/n \n')
		
		if segirIns == 'n':
			insertar = False



query= "SELECT * FROM Victimas WHERE 1;"
micursor.execute(query)

# Obtenemos el resultado con fetchall
registros= micursor.fetchall()

for registro in registros:
	print registro["Nombre"] + " es del tipo " + registro["Profesion"]


query= "DELETE FROM Victimas WHERE 1;"
micursor.execute(query)
micursor.close () 
Conexion.close () 