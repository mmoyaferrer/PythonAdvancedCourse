import re
## Manuel Moya Ferrer
## Curso Python avanzado
## Ejercicio Expresiones regulares - Identificar Fecha

cadena= "A fecha Granada 25/Ago/2012 22:23 PM se descubrio la cura de una nueva enfermedad"


########  NOMBRE CIUDAD           DIA       MES                                                    ANIO      HORA   MINUTO  AM|PM    ######################
patron="[a-zA-Z]+\s?[a-zA-Z]+\s"+"\d\d?[/](Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dic)/[2-9]\d{3}\s"+"\d\d?[:]\d\d?\s(AM|PM)"

if re.search(patron, cadena, re.M):
    print "Fecha encontrada"
else:
    print "No aparece ninguna fecha"