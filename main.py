# -*- coding: utf-8 -*-

# Proyecto 2 Sistemas Difusos
# Profesor: Claudio Held
# Auxiliar: Leonardo Causa
# Estudiante: Matías Osses
# Estudiante: Alvaro Toledo

from objetos import base_de_reglas, base_de_hechos, hipotesis
from clases import *
from utils import *

sistema = Sistema(base_de_hechos, base_de_reglas, hipotesis)
print(sistema)