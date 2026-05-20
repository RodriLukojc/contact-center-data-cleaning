# Contact Center Data Cleaning

## Descripción del proyecto
Este proyecto simula un proceso real de **limpieza y análisis de datos operativos** de un Contact Center.  
El objetivo es mostrar un flujo completo de trabajo en Python y Jupyter Notebook, desde la generación de datos hasta la normalización y exploración visual.

---

## Objetivos
- Generar una base operativa con errores intencionales (valores nulos, duplicados, formatos inconsistentes).  
- Aplicar un script de limpieza (src/cleaning.py) para normalizar los datos.  
- Realizar un análisis exploratorio (EDA) en notebooks/eda.ipynb  
- Comparar la base original vs CLEAN y documentar los hallazgos.  

---

## Estructura del repositorio

contact-center-data-cleaning/
│
├── data/
│   ├── raw/ → base_operativa.csv
│   └── processed/ → base_operativa_clean.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── cleaning.py
│   └── README.md
│
└── README.md

Código

---

## ⚙️ Tecnologías utilizadas
- Python 3.13  
- Pandas  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio:

git clone https://github.com/rodrigolukojc/contact-center-data-cleaning.git

Instalar dependencias:

pip install -r requirements.txt

Generar la base sucia:

python src/script_generar_base_operativa_random.py

Limpiar los datos:

python src/cleaning.py

Explorar resultados:

Abrir notebooks/eda.ipynb en VS Code o Jupyter.

📈 Resultados esperados

Reducción de registros inválidos y duplicados.

Normalización de fechas y teléfonos.

Visualización clara de agentes y resultados.

Comparación cuantitativa entre base original y CLEAN.

👨‍💻 Autor
Rodrigo Lukojc  


🧾 Licencia
Este proyecto se distribuye bajo la licencia MIT.
