import pandas as pd
import random
from datetime import datetime, timedelta

# Parámetros
n = 500
agentes = ["Ana", "Juan", "Pedro", "Lucía", "Marcos", None]
resultados = ["Contactado", "No contesta", "Error", "Fuera de servicio", "Contactado ", "No contesta "]
productos = ["A", "B", "C"]

def random_phone():
    formatos = [
        "11-5555-" + str(random.randint(1000, 9999)),
        "115555" + str(random.randint(1000, 9999)),
        "11 " + str(random.randint(55550000, 55559999)),
        "+54 11 5555 " + str(random.randint(1000, 9999)),
        ""
    ]
    return random.choice(formatos)

def random_date():
    base = datetime(2024, 1, 1)
    delta = timedelta(days=random.randint(0, 30))
    formatos = ["%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%Y-13-%d"]
    return (base + delta).strftime(random.choice(formatos))

def random_importe():
    valores = [None, random.randint(1000, 2000), "error", ""]
    return random.choice(valores)

data = []
for i in range(1, n + 1):
    fila = [
        f"{i:03d}",
        random_phone(),
        random_date(),
        random.choice(resultados),
        random.choice(agentes),
        random_importe(),
        random.choice(productos)
    ]
    data.append(fila)

df = pd.DataFrame(data, columns=["id_cliente","telefono","fecha_contacto","resultado","agente","importe","producto"])

# Agregar duplicados intencionales
df = pd.concat([df, df.sample(frac=0.05)], ignore_index=True)

# Guardar CSV
df.to_csv("data/raw/base_operativa.csv", index=False)
print("✔ Archivo generado con", len(df), "registros.")
