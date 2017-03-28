# -*- coding: utf-8 -*-

import MySQLdb

# Establecemos la conexión
Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')

# Creamos el cursor, pero especificando que sea de la subclase DictCursor
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)

# Insertamos un par de registros
query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (1, \"Ejercito de Zombies\",\"Muertos Vivientes\",\"Desmembramiento a espada\");"

micursor.execute(query)

query= "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (2, \"Vampiro feo\",\"Muertos Vivientes\",\"Estaca de madera\");"

micursor.execute(query)

# Ahora vamos a hacer un SELECT
query= "SELECT * FROM Victimas WHERE 1;"

micursor.execute(query)

# Obtenemos el resultado con fetchall
registros= micursor.fetchall()

for registro in registros:

# ... imprimimos el registro...
 print registro["Nombre"] + " es del tipo " + registro["Profesion"]

# Esto que sigue es para borrar el contenido de la base de datos,
# y que no se nos acumule al ir haciendo pruebas
query= "DELETE FROM Victimas WHERE 1;"

micursor.execute(query)

Conexion.commit()

micursor.close()
Conexion.close()

