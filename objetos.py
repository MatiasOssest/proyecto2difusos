# -*- coding: utf-8 -*-
from clases import Tripleta, BaseHecho, Hecho, Regla, BaseReglas, Premisa

base_de_hechos = BaseHecho()
base_de_reglas = BaseReglas()
hipotesis = BaseHecho()

animal = "animal"
da = "da"
es = "es"
tiene = "tiene"

# Regla 1
p1 = Tripleta(animal, tiene, "pelo")

t1 = Tripleta(animal, es, "mamífero")
t2 = Tripleta(animal, es, "ave")
t3 = Tripleta(animal, es, "reptil")

h1 = Hecho(t1, 0.8)
h2 = Hecho(t2, -1.0)
h3 = Hecho(t3, -1.0)

premisa = Premisa(p1)
conclusion = BaseHecho(h1, h2, h3)

r = Regla("R1", premisa, conclusion)
base_de_reglas.agregar_regla(r)

# Regla 2

p1 = Tripleta(animal, da, "leche")

premisa = Premisa(p1)

h1 = Hecho(t1, 1.0)
h2 = Hecho(t2, -1.0)
h3 = Hecho(t3, -1.0)

conclusion = BaseHecho(h1, h2, h3)

r = Regla("R2", premisa, conclusion)
base_de_reglas.agregar_regla(r)

# Regla 3

p1 = Tripleta(animal, "pone", "huevos")
p2 = Tripleta(animal, tiene, "piel dura")
premisa = Premisa(p1, p2)

h1 = Hecho(t1, -1.0)
h2 = Hecho(t2, -1.0)
h3 = Hecho(t3, 1.0)

conclusion = BaseHecho(h1, h2, h3)

r = Regla("R3", premisa, conclusion)
base_de_reglas.agregar_regla(r)

# Regla 4

p1 = Tripleta(animal, "pone", "huevos")
p2 = Tripleta(animal, "puede", "volar")
premisa = Premisa(p1, p2)

h2 = Hecho(t2, 1.0)
h3 = Hecho(t3, -1.0)

conclusion = BaseHecho(h2, h3)

r = Regla("R4", premisa, conclusion)
base_de_reglas.agregar_regla(r)

# Regla 5

p1 = Tripleta(animal, tiene, "plumas")
premisa = Premisa(p1)
h1 = Hecho(t1, -1.0)
h2 = Hecho(t2, 1.0)
h3 = Hecho(t3, -1.0)

conclusion = BaseHecho(h1, h2, h3)
r = Regla("R5", premisa, conclusion)
base_de_reglas.agregar_regla(r)

# Regla 6

p1 = Tripleta(animal, "come", "carne")
premisa = Premisa(p1)

carnivoro = Tripleta(animal, es, "carnívoro")
h1 = Hecho(carnivoro, 1.0)

conclusion = BaseHecho(h1)
r = Regla("R6", premisa, conclusion)
base_de_reglas.agregar_regla(r)

# Regla 7

p1 = Tripleta(animal, tiene, "garras")
premisa = Premisa(p1)

h1 = Hecho(carnivoro, 0.8)
conclusion = BaseHecho(h1)

r = Regla("R7", premisa, conclusion)
base_de_reglas.agregar_regla(r)

# Regla 8

p1 = Tripleta(animal, es, "mamífero")
p2 = Tripleta(animal, tiene, "pezuñas")
premisa = Premisa(p1, p2)

t1 = Tripleta(animal, es, "ungulado")

h1 = Hecho(t1, 1.0)

conclusion = BaseHecho(h1)
r = Regla("R8", premisa, conclusion)
base_de_reglas.agregar_regla(r)

# Regla 9

p1 = Tripleta(animal, es, "mamífero")
p2 = Tripleta(animal, es, "rumiante")
premisa = Premisa(p1, p2)

h1 = Hecho(t1, 0.75)

conclusion = BaseHecho(h1)
r = Regla("R9", premisa, conclusion)
base_de_reglas.agregar_regla(r)

# Regla 10

p1 = Tripleta(animal, "vive", "con personas")
premisa = Premisa(p1)

t1 = Tripleta(animal, es, "doméstico")
h1 = Hecho(t1, 0.9)

conclusion = BaseHecho(h1)
r = Regla("R10", premisa, conclusion)
base_de_reglas.agregar_regla(r)

# Regla 11

p1 = Tripleta(animal, "vive", "en zoológico")
premisa = Premisa(p1)
h1 = Hecho(t1, -0.8)

conclusion = BaseHecho(h1)
r = Regla("R11", premisa, conclusion)
base_de_reglas.agregar_regla(r)

# Regla 12

p1 = Tripleta(animal, es, "mamífero")
p2 = Tripleta(animal, es, "carnívoro")
p3 = Tripleta(animal, tiene, "manchas oscuras", True)
premisa = Premisa(p1, p2, p3)

t1 = Tripleta(animal, es, "cheetah")
h1 = Hecho(t1, 0.9)
h2 = Hecho(t1, 0.9)

conclusion = BaseHecho(h1)
r = Regla("R12", premisa, conclusion)
base_de_reglas.agregar_regla(r)
hipotesis.agregar_hecho(h2)

# Regla 13

p1 = Tripleta(animal, es, "mamífero")
p2 = Tripleta(animal, es, "carnívoro")
p3 = Tripleta(animal, tiene, "rayas negras", True)
premisa = Premisa(p1, p2, p3)

t1 = Tripleta(animal, es, "tigre")
h1 = Hecho(t1, 0.85)
h2 = Hecho(t1, 0.85)

conclusion = BaseHecho(h1)
r = Regla("R13", premisa, conclusion)
base_de_reglas.agregar_regla(r)
hipotesis.agregar_hecho(h2)

# Regla 14

p1 = Tripleta(animal, es, "mamífero")
p2 = Tripleta(animal, es, "carnívoro")
p3 = Tripleta(animal, es, "doméstico")
premisa = Premisa(p1, p2, p3)

t1 = Tripleta(animal, es, "perro")
h1 = Hecho(t1, 0.9)
h2 = Hecho(t1, 0.9)

conclusion = BaseHecho(h1)
r = Regla("R14", premisa, conclusion)
base_de_reglas.agregar_regla(r)
hipotesis.agregar_hecho(h2)

# Regla 15

p1 = Tripleta(animal, es, "reptil")
p2 = Tripleta(animal, es, "doméstico")

premisa = Premisa(p1, p2)

t1 = Tripleta(animal, es, "tortuga")
h1 = Hecho(t1, 0.7)
h2 = Hecho(t1, 0.7)

conclusion = BaseHecho(h1)
r = Regla("R15", premisa, conclusion)
base_de_reglas.agregar_regla(r)
hipotesis.agregar_hecho(h2)

# Regla 16

p1 = Tripleta(animal, es, "mamífero")
p2 = Tripleta(animal, es, "ungulado")
p3 = Tripleta(animal, tiene, "cuello largo", True)
premisa = Premisa(p1, p2, p3)

t1 = Tripleta(animal, es, "jirafa")
h1 = Hecho(t1, 1.0)
h2 = Hecho(t1, 1.0)

conclusion = BaseHecho(h1)
r = Regla("R16", premisa, conclusion)
base_de_reglas.agregar_regla(r)
hipotesis.agregar_hecho(h2)

# Regla 17

p1 = Tripleta(animal, es, "mamífero")
p2 = Tripleta(animal, es, "ungulado")
p3 = Tripleta(animal, tiene, "rayas negras", True)
premisa = Premisa(p1, p2, p3)

t1 = Tripleta(animal, es, "cebra")
h1 = Hecho(t1, 0.95)
h2 = Hecho(t1, 0)

conclusion = BaseHecho(h1)
r = Regla("R17", premisa, conclusion)
base_de_reglas.agregar_regla(r)
hipotesis.agregar_hecho(h2)

# Regla 18

p1 = Tripleta(animal, es, "mamífero")
p2 = Tripleta(animal, "puede", "volar")
p3 = Tripleta(animal, es, "feo", True)
premisa = Premisa(p1, p2, p3)

t1 = Tripleta(animal, es, "murciélago")
h1 = Hecho(t1, 0.9)
h2 = Hecho(t1, 0)

conclusion = BaseHecho(h1)
r = Regla("R18", premisa, conclusion)
base_de_reglas.agregar_regla(r)
hipotesis.agregar_hecho(h2)

# Regla 19

p1 = Tripleta(animal, es, "ave")
p2 = Tripleta(animal, "vuela", "bien", True)

premisa = Premisa(p1, p2)

t1 = Tripleta(animal, es, "gaviota")
h1 = Hecho(t1, 0.9)
h2 = Hecho(t1, 0)

conclusion = BaseHecho(h1)
r = Regla("R19", premisa, conclusion)
base_de_reglas.agregar_regla(r)
hipotesis.agregar_hecho(h2)

# Regla 20

p1 = Tripleta(animal, es, "ave")
p2 = Tripleta(animal, "corre", "rápido", True)
premisa = Premisa(p1, p2)

t1 = Tripleta(animal, es, "avestruz")
h1 = Hecho(t1, 1.0)
h2 = Hecho(t1, 0)

conclusion = BaseHecho(h1)
r = Regla("R20", premisa, conclusion)
base_de_reglas.agregar_regla(r)
hipotesis.agregar_hecho(h2)

# Regla 21

p1 = Tripleta(animal, es, "ave")
p2 = Tripleta(animal, es, "parlanchín", True)
premisa = Premisa(p1, p2)

t1 = Tripleta(animal, es, "loro")
h1 = Hecho(t1, 0.95)
h2 = Hecho(t1, 0)

conclusion = BaseHecho(h1)
r = Regla("R21", premisa, conclusion)
base_de_reglas.agregar_regla(r)
hipotesis.agregar_hecho(h2)

# Regla 22

p1 = Tripleta(animal, es, "mamífero")
p2 = Tripleta(animal, es, "grande", True)
p3 = Tripleta(animal, es, "ungulado")
p4 = Tripleta(animal, tiene, "trompa", True)
premisa = Premisa(p1, p2, p3, p4)

t1 = Tripleta(animal, es, "elefante")
h1 = Hecho(t1, 0.9)
h2 = Hecho(t1, 0)

conclusion = BaseHecho(h1)
r = Regla("R22", premisa, conclusion)
base_de_reglas.agregar_regla(r)
hipotesis.agregar_hecho(h2)

hipotesis.reset_vc()
