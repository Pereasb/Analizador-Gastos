import pandas as pd
import sys

def cargar_datos(ruta_archivo):
    try:
        return pd.read_csv(ruta_archivo)

    except FileNotFoundError:
        print(f"Error: no existe el archivo '{ruta_archivo}'")
        sys.exit(1)

def validar_columnas(df):
    columnas_requeridas = [
        "fecha",
        "categoria",
        "monto"
    ]

    for columna in columnas_requeridas:
        if columna not in df.columns:
            print(f"Error: falta la columna '{columna}'")
            sys.exit(1)


def calcular_gastos_por_categoria(df):
    return df.groupby("categoria")["monto"].sum()


def calcular_total_gastos(df):
    return df["monto"].sum()

def formatear_categorias(gastos_por_categoria):
    categorias = ""
    for categoria, monto in gastos_por_categoria.items():
        categorias += f"{categoria}: ${monto}\n"
    return categorias

def calcular_categoria_mayor_gasto(gastos_por_categoria):
    return gastos_por_categoria.idxmax()

def generar_reporte(total, categorias_formateadas, categoria_mayor_gasto):
    return f"""REPORTE DE GASTOS

Total gastado:
${total}

Categorías de gasto:
{categorias_formateadas}

Categoría con mayor gasto:
{categoria_mayor_gasto}
"""

def guardar_reporte(reporte):
    with open("reportes/reporte_gastos.txt", "w") as archivo:
        archivo.write(reporte)


def main():
    if len(sys.argv) < 2:
        print("Uso: python src/main.py archivo.csv")
        sys.exit(1)

    df = cargar_datos(sys.argv[1])
    validar_columnas(df)
    gastos_por_categoria = calcular_gastos_por_categoria(df)
    total = calcular_total_gastos(df)
    categorias_formateadas = formatear_categorias(gastos_por_categoria)
    categoria_mayor_gasto = calcular_categoria_mayor_gasto(gastos_por_categoria)
    reporte = generar_reporte(total, categorias_formateadas, categoria_mayor_gasto)
    guardar_reporte(reporte)

if __name__ == "__main__":
    main()