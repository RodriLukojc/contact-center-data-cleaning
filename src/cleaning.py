import pandas as pd
from datetime import datetime

RAW_PATH = "data/raw/base_operativa.csv"
PROCESSED_PATH = "data/processed/base_operativa_clean.csv"

def normalize_phone(phone):
    if pd.isna(phone):
        return None
    digits = "".join(filter(str.isdigit, str(phone)))
    return digits if len(digits) >= 10 else None

def parse_date(date):
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y"):
        try:
            return datetime.strptime(date, fmt).date()
        except:
            pass
    return None

def clean_data():
    df = pd.read_csv(RAW_PATH)

    # Trim y normalización básica
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Normalizar teléfono
    df["telefono"] = df["telefono"].apply(normalize_phone)

    # Normalizar fecha
    df["fecha_contacto"] = df["fecha_contacto"].apply(parse_date)

    # Convertir importe a numérico
    df["importe"] = pd.to_numeric(df["importe"], errors="coerce")

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Eliminar filas sin teléfono o fecha válida
    df = df.dropna(subset=["telefono", "fecha_contacto"])

    # Completar agente faltante
    df["agente"] = df["agente"].fillna("SIN_ASIGNAR")

    df.to_csv(PROCESSED_PATH, index=False)
    print("✔ Base procesada y guardada en:", PROCESSED_PATH)

if __name__ == "__main__":
    clean_data()
