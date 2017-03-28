import re
patron = "manch\d"
cadena= "En un lugar de la mancha de cuyo nombre no quiero acordarme"
if re.search(patron, cadena, re.M):
    print "Lo encontre, que cosas"
else:
    print "No aparece"