# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 18:14:08 2025

@author: villesca
"""

import pandas as pd

# Cargar el archivo Excel (especifica la ruta correcta del archivo)
file_path = 'C:/Users/ville/datos_qcos.xlsx'  # Cambia esto por la ubicación de tu archivo
df = pd.read_excel(file_path, skiprows=3, header=0)
#print(df.head())

#print(df.columns)

#conteo_valores = df['Recurso'].value_counts()
#print(conteo_valores)

#sin_info = df[df['Recurso'] == 'S/I']  # DataFrame filtrado
#desconocido = df[df['Recurso'] == 'DESCONOCIDO'] 
#df_rec = df.drop(sin_info.index)
#df_rec = df.drop(desconocido.index)

#conteo_rec = df_rec['Recurso'].value_counts()
#print(conteo_rec)


import re


def limpiar_recursos(recurso):
    """
    Limpia y estandariza los nombres de recursos
    Maneja múltiples separadores y elimina duplicados
    """
    if pd.isna(recurso):
        return recurso
    
    # Convertir a minúsculas y quitar espacios
    recurso_limpio = str(recurso).lower().strip()
    
    # Definir múltiples separadores usando regex
    # Busca: guión, 'y', '&', '+', coma, punto y coma
    patron_separadores = r'[-y&+,;]\s*|\s+y\s+|\s+&\s+|\s+\+\s+'
    
    # Dividir usando el patrón de separadores
    recursos = re.split(patron_separadores, recurso_limpio)
    
    # Limpiar cada recurso individual
    recursos_limpios = []
    for r in recursos:
        r = r.strip()
        if r and r not in recursos_limpios:  # Eliminar duplicados y strings vacíos
            recursos_limpios.append(r)
    
    # Si solo hay un recurso, devolverlo directamente
    if len(recursos_limpios) == 1:
        return recursos_limpios[0]
    
    # Si hay múltiples recursos, ordenarlos alfabéticamente
    if len(recursos_limpios) > 1:
        recursos_limpios.sort()
        return ' y '.join(recursos_limpios)
    
    return recurso_limpio

# Aplicar la función de limpieza
df['recurso_limpio'] = df['Recurso'].apply(limpiar_recursos)

print("\nDataFrame después de la limpieza:")
print(df)

# Ver los valores únicos para verificar
print("\nValores únicos después de la limpieza:")
print(df['recurso_limpio'].unique())

# Contar frecuencias
print("\nFrecuencias de cada recurso:")
print(df['recurso_limpio'].value_counts())

def filtrar_recursos_validos(df, columna_recurso='recurso'):
    """
    Elimina filas que contienen valores no válidos en la columna de recursos
    
    Parámetros:
    - df: DataFrame a filtrar
    - columna_recurso: nombre de la columna con los recursos
    
    Retorna:
    - DataFrame filtrado sin los valores no válidos
    """
    # Valores a eliminar (en minúsculas para comparación)
    valores_a_eliminar = [
        's/i', 'si', 'desconocido', 'unknown', 
        'sin información', 'sin informacion',
        'no especificado', 'no especifica',
        'n/a', 'na', 'null', 'none', 'vacio', 
        'sin dato', 'sin datos', 'no aplica',
        'no disponible', 'no dato', 'nd'
    ]
    
    # Crear una copia del DataFrame
    df_filtrado = df.copy()
    
    # Función para verificar si un valor debe eliminarse
    def es_valor_valido(valor):
        if pd.isna(valor):
            return False  # Eliminar valores nulos/NaN
        
        valor_limpio = str(valor).lower().strip()
        
        # Verificar si el valor está en la lista de valores a eliminar
        return valor_limpio not in valores_a_eliminar
    
    # Filtrar el DataFrame
    mask_validos = df_filtrado[columna_recurso].apply(es_valor_valido)
    df_filtrado = df_filtrado[mask_validos]
    
    return df_filtrado


# Filtrar valores no válidos
df_final = filtrar_recursos_validos(df, 'recurso_limpio')


print("\nDespués de filtrar valores no válidos:")
print(df_final)


print("\nRecursos únicos finales:")
print(df_final['recurso_limpio'].unique())