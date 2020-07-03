# -*- coding: utf-8 -*-

# Proyecto 2 Sistemas Difusos
# Profesor: Claudio Held
# Auxiliar: Leonardo Causa
# Estudiante: Matías Osses
# Estudiante: Alvaro Toledo

import json

from objetos import base_de_reglas, base_de_hechos, hipotesis
from clases import *
from utils import *


sistema = Sistema(base_de_hechos, base_de_reglas, hipotesis)

with open("preguntas.json", encoding="utf-8") as f:
    preguntas = json.load(f)

clases = obtener_clases(preguntas)
print(clases)

sistema.base_hechos.agregar_hecho(hipotesis)
actual = sistema.base_hechos.get_last()
print(actual[1])