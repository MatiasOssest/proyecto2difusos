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

with open("preguntas.json", encoding="utf-8") as f:
    preguntas = json.load(f)


def generaPreguntas(pregs):
    for pregunta in pregs:
        yield pregunta

p = generaPreguntas(preguntas)
clases = obtener_clases(preguntas)
print(base_de_reglas)
entrada = "y"
while entrada == "y":
    sistema = Sistema(base_de_hechos, base_de_reglas, hipotesis)
    sistema.evaluar()
    entrada = input("desea intentar de nuevo ? [y/n]")