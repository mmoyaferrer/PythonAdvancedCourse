# -*- coding: utf-8 -*-
#################################
#################################
###    MANUEL MOYA FERRER     ###
#################################
#################################

from gi.repository import Gtk, GObject
import MySQLdb

class tareasSQL_GUI:

	def __init__(self):
		
		self.conectarBaseDatosSQL()
		print "Conectado a base de datos"
		self.builder=Gtk.Builder()
		self.builder.add_from_file("interfazgladeplanificaciontareas.glade")
		self.handlers={"onDeleteWindow":Gtk.main_quit,
						"onCrearTarea":self.onCrearTarea,
						"onObtenerTarea":self.onObtenerTarea,
						"onActualizarTarea":self.onActualizarTarea,
						"onBorrarTarea":self.onBorrarTarea,
						"onAcercaDe":self.onAcercaDe,
						"cerrarOnAcercaDe":self.cerrarOnAcercaDe}
		self.builder.connect_signals(self.handlers)

		self.window=self.builder.get_object("window1")
		self.window.show_all()

		self.about=self.builder.get_object("aboutdialog")

	def onAcercaDe(self,menuitem):
		self.about.show()
		pass

	def cerrarOnAcercaDe(self,menuitem):
		self.about.hide()
		print "cerrar"
		pass


	def conectarBaseDatosSQL(self):
		# Establecemos la conexión
		self.Conexion = MySQLdb.connect(host='localhost', user='manuel',passwd='moya', db='DBtareas')
		#El tipo de la tabla existente en la base de datos es --> 
		#CREATE TABLE Tareas (id INT,Tarea VARCHAR(100),Dia VARCHAR(100),Mes VARCHAR(100),Anio VARCHAR(1000));
		#Creamos el cursor
		self.micursor = self.Conexion.cursor(MySQLdb.cursors.DictCursor)
		self.Conexion.commit()
		query= "INSERT INTO PlanificacionTareas (id,Tarea,Dia,Mes,Anio,Prioridad) VALUES (1, \"Nacer\",1,12,1994,1);"
		self.micursor.execute(query)
		self.Conexion.commit()
	

	def onCrearTarea(self,meuitem):
		print "Crear Tarea"
		entryID=self.builder.get_object("entryID")
		entryTarea=self.builder.get_object("entryTarea")
		entryDia=self.builder.get_object("entryDia")
		entryMes=self.builder.get_object("entryMes")
		entryAnio=self.builder.get_object("entryAnio")
		entryPrioridad=self.builder.get_object("entryPrioridad")
		
		idAEscribir=int(entryID.get_text())
		Tarea=entryTarea.get_text()
		Dia=int(entryDia.get_text())
		Mes=int(entryMes.get_text())
		Anio=int(entryAnio.get_text())
		Prioridad=int(entryPrioridad.get_text())

		#print "El id ingresado es :" + entryID.get_text()
		query= "INSERT INTO PlanificacionTareas (id,Tarea,Dia,Mes,Anio,Prioridad) VALUES (%d, %s,%d,%d,%d,%d);"% (idAEscribir,"\""+Tarea+"\"",Dia,Mes,Anio,Prioridad)
		self.micursor.execute(query)
		self.Conexion.commit()
		pass
	
	def onObtenerTarea(self,menuitem):
		print "Obtener Tarea"
		entryID=self.builder.get_object("entryID")
		idALeer=int(entryID.get_text())
		query= "SELECT * FROM PlanificacionTareas WHERE id=%d;"%(idALeer)
		self.micursor.execute(query)
		self.Conexion.commit()
		registro=self.micursor.fetchone()
		
		Tarea=registro["Tarea"]
		Dia=registro["Dia"]
		Mes=registro["Mes"]
		Anio=registro["Anio"]
		Prioridad=registro["Prioridad"]

		entryTarea=self.builder.get_object("entryTarea")
		entryDia=self.builder.get_object("entryDia")
		entryMes=self.builder.get_object("entryMes")
		entryAnio=self.builder.get_object("entryAnio")
		entryPrioridad=self.builder.get_object("entryPrioridad")

		entryTarea.set_text(Tarea)
		entryDia.set_text(str(Dia))
		entryMes.set_text(str(Mes))
		entryAnio.set_text(str(Anio))
		entryPrioridad.set_text(str(Prioridad))

		pass
	
	def onActualizarTarea(self,menuitem):
		
		print "Actualizar Tarea"

		entryID=self.builder.get_object("entryID")
		entryTarea=self.builder.get_object("entryTarea")
		entryDia=self.builder.get_object("entryDia")
		entryMes=self.builder.get_object("entryMes")
		entryAnio=self.builder.get_object("entryAnio")
		entryPrioridad=self.builder.get_object("entryPrioridad")
		
		idAActualizar=int(entryID.get_text())
		Tarea=entryTarea.get_text()
		Dia=int(entryDia.get_text())
		Mes=int(entryMes.get_text())
		Anio=int(entryAnio.get_text())
		Prioridad=int(entryPrioridad.get_text())

		query="UPDATE PlanificacionTareas SET Tarea=%s, Dia=%d, Mes=%d, Anio=%d, Prioridad=%d WHERE id=%d;"%("\""+Tarea+"\"",Dia,Mes,Anio,Prioridad,idAActualizar)
		self.micursor.execute(query)
		self.Conexion.commit()


		pass

	def onBorrarTarea(self,menuitem):
		print "Borrar Tarea"
		entryID=self.builder.get_object("entryID")
		idALeer=int(entryID.get_text())
		query= "DELETE FROM PlanificacionTareas WHERE id=%d;"%(idALeer)
		self.micursor.execute(query)
		self.Conexion.commit()
		pass
	


	def mostrarRegistros(self):


		print "\nRegistros mostrados a continuacion\n"
		# Ahora vamos a hacer un SELECT
		query= "SELECT * FROM PlanificacionTareas WHERE 1;"
		micursor.execute(query)
		Conexion.commit()

		registros= micursor.fetchall()
				
		for registro in registros:
			print registro["Tarea"] + " el dia " + str(registro["Dia"]) + " de " + str(registro["Mes"]) + " del anio " + str(registro["Anio"])
			pass
				
		
	def borrarDatos(self):
		query= "DELETE FROM PlanificacionTareas WHERE 1;"
		micursor.execute(query)
		Conexion.commit()

tarea=tareasSQL_GUI()


Gtk.main()