# clasificacion_variables.py — Parte A: clasificación de las variables de clientes.csv.
#
# El archivo data/clientes.csv tiene 12 clientes y 7 variables (más el id).
# El objetivo: clasificar cada variable (numérica continua/discreta, categórica
# binaria/ordinal/nominal) y verificar la clasificación en código.
#
# Regla del capítulo 3: el dtype es una pista, no la clasificación — el criterio
# (¿tiene sentido la mitad del valor? ¿hay orden entre las categorías?) decide.
#
# Uso (desde la raíz del repositorio):  python scripts/clasificacion_variables.py

import pandas as pd

clientes = pd.read_csv("data/clientes.csv")

# ---------------------------------------------------------------------------
# 1. Estructura del archivo
# ---------------------------------------------------------------------------
print(f"Dimensiones: {clientes.shape[0]} filas × {clientes.shape[1]} columnas")
print()
print("Primeras filas:")
print(clientes.to_string(index=False))
print()

# ---------------------------------------------------------------------------
# 2. Tipos inferidos (dtype) — la pista que da el lenguaje
# ---------------------------------------------------------------------------
print("Tipos inferidos (dtype):")
print(clientes.dtypes)
print()
# TODO 1: ¿qué columnas llegan como número y cuáles como texto? Anótalo para el
#         informe. Ojo con satisfaccion: llega como número y es ordinal
#         ("4 no es el doble de 2") — la justificación va en el informe.

# ---------------------------------------------------------------------------
# 3. Valores únicos — ¿cuántas categorías hay y cuáles son?
# ---------------------------------------------------------------------------
# TODO 2: completa el bucle para imprimir, por columna, cuántos valores únicos
#         hay y cuáles son. Pista: for columna in clientes.columns: ...  con
#         clientes[columna].unique() y len(). ¿Cuántas categorías tiene genero?
for columna in clientes.columns:
    valores = sorted(clientes[columna].unique().tolist())
    print(f"{columna}: {len(valores)} únicos -> {valores}")
print()

# TODO 3: nivel_educacion como categoría ordenada
orden_edu = ["Primaria", "Secundaria", "Universidad", "Posgrado"]
clientes["nivel_educacion"] = clientes["nivel_educacion"].astype(
    pd.CategoricalDtype(categories=orden_edu, ordered=True))
print("Mínimo de nivel_educacion:", clientes["nivel_educacion"].min())

# TODO 4: satisfaccion como categoría ordenada (escala 1-5)
clientes["satisfaccion"] = clientes["satisfaccion"].astype(
    pd.CategoricalDtype(categories=[1, 2, 3, 4, 5], ordered=True))
print("Mínimo de satisfaccion:", clientes["satisfaccion"].min())

# Prueba extra: el typo "Postgrado" (con t) falla en silencio
orden_typo = ["Primaria", "Secundaria", "Universidad", "Postgrado"]
con_typo = clientes["nivel_educacion"].astype(str).astype(
    pd.CategoricalDtype(categories=orden_typo, ordered=True))
print("Faltantes por el typo:", con_typo.isna().sum())
print()

# ---------------------------------------------------------------------------
# 5. Resumen de la clasificación (para el informe)
# ---------------------------------------------------------------------------
# TODO 5: completa el resumen con el tipo de cada variable (el criterio que
#         justifica cada clasificación va en el informe).
clasificacion = {
    "cliente_id": "identificador",
    "edad": "cuantitativa continua",
    "numero_hijos": "cuantitativa discreta",
    "genero": "cualitativa nominal",
    "nivel_educacion": "cualitativa ordinal",
    "ciudad": "cualitativa nominal",
    "ingresos_mensuales": "cuantitativa continua",
    "satisfaccion": "cualitativa ordinal",
}
print("Resumen de la clasificación (para el informe):")
for variable, tipo in clasificacion.items():
    print(f"  {variable:20s} {tipo}")
