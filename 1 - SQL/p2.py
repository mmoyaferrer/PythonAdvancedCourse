# -*- coding: utf-8 -*-

import MySQLdb

# Establecemos la conexión
Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')

# Creamos el cursor
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)

# R1
# Insertamos algunos registros (de forma cutre e ineficiente) para tener con qué trabajar
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (1, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");"

micursor.execute(query)

# R2
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (2, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"

micursor.execute(query)

# R3
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (3, \"Vampiro guapo\",\"Muertos Vivientes\",\"Estaca de plata\");"

micursor.execute(query)

# R4
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (4, \"Bestia del Pantano\",\"Monstruo\",\"Destripado\");"

micursor.execute(query)

# R5
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (5, \"Serpiente\",\"Monstruo\",\"Destripado\");"

micursor.execute(query)

# R6
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (6, \"Dracula\",\"Muerto viviente\",\"Desmembramiento a espada\");"

micursor.execute(query)

# R7
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (7, \"Dinosaurio\",\"Animal\",\"Muerte por asfixia\");"

micursor.execute(query)

# R8
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (8, \"Hamster\",\"Animal\",\"Muerte por hambre\");"

micursor.execute(query)

# R9
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (9, \"Gremlin\",\"Monstruo\",\"Exceso de agua\");"

micursor.execute(query)



# R10
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (10, \"Loki\",\"Dios de la mitologia nordica\",\"Desmembramiento a espada\");"
print query

micursor.execute(query)



#Fin de los registros automaticos
# Hacemos un commit, por si las moscas
Conexion.commit()

numero=-1
idAEscribir=11

while (numero!=0):

	numero = input("\nPulsa 1 para introducir un nuevo registro | Pulsa 2 para ver los registros existentes | Pulsa 0 para salir del programa\n")

	if numero==1:
		Nombre	=	raw_input("Introduce el nombre\n")
		Profesion	=	raw_input("Introduce la profesion\n")
		Muerte	=	raw_input("Introduce la muerte\n")
		
		
		query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (%d, %s,%s,%s);"% (idAEscribir,"\""+Nombre+"\"","\""+Profesion+"\"","\""+Muerte+"\"")
		
		

		if Nombre=="" or Profesion=="" or Muerte=="":
			print "Uno de los campos introducidos está en blanco, no se introducira el registro"
			pass
		else:
			print query
			micursor.execute(query)
			Conexion.commit()
			idAEscribir=idAEscribir+1
			print "\nRegistro agregado\n"
		pass
		#introducir un nuevo registro
	
	elif	numero==2:	
		print "\""+"Registros mostrados a continuacion"+"\""
		# Ahora vamos a hacer un SELECT
		query= "SELECT * FROM Victimas WHERE 1;"
		micursor.execute(query)
		Conexion.commit()

		registros= micursor.fetchall()
		Conexion.commit()
		for registro in registros:
			print registro["Nombre"] + " es del tipo " + registro["Profesion"]
		pass
		
		#ver registros existentes
	elif	numero==0:
		pass
		#salir del programa

	

# Esto que sigue es para borrar el contenido de la base de datos,
# y que no se nos acumule al ir haciendo pruebas
#query= "DELETE FROM Victimas WHERE 1;"
#micursor.execute(query)
#Conexion.commit()

#cadena = raw_input(“Introduce una cadena de texto: “)
#print “La cadena que ingreso es:\n”,cadena

