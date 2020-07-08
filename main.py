# -*- coding: utf-8 -*-

# Proyecto 2 Sistemas Difusos
# Profesor: Claudio Held
# Auxiliar: Leonardo Causa
# Estudiante: Matías Osses
# Estudiante: Alvaro Toledo

import json

from objetos import base_de_reglas, base_de_hechos, hipotesis
from clases import Sistema

entrada = "y"
while entrada == "y":
    base_de_hechos.limpiar()
    hipotesis.reset_vc()
    sistema = Sistema(base_de_hechos, base_de_reglas, hipotesis)
    sistema.evaluar()

    entrada = input("¿Desea jugar otra vez? [y/n]")