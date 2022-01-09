# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 22:36:50 2022

@author: salv-
"""
#Importamos el mpdulo pandas para trabajar los datos
import pandas as pd
#%% Lector de la base de datos
#Mandamos llamar el archivo donde tenemos la base de datos, para su analisis 

synergy_dataframe = pd.read_csv('synergy_logistics_database.csv', index_col=0, 
                                encoding='utf-8')

valor_total= sum()['total_value']

#%% Primer ejercicio 

#Se hacen dos casos para mandar llamar los datos por 'direction' para así poder separarlos posteriormente
# en exportaciones e importaciones

exports = synergy_dataframe[synergy_dataframe['direction'] == 'Exports']
imports = synergy_dataframe[synergy_dataframe['direction'] == 'Imports']

#Creamos una funcion que combine los tres grupos de datos que nesecitamos y 
#los combine, también sumamos el 'total_value' por grupo de datos y los 
#ordenamos de mayor a menor
def rutas(df):
    combinaciones_rutas = df.groupby(by=['direction', 'origin','destination']).sum()['total_value'].reset_index()
    combinaciones_sort= combinaciones_rutas.sort_values( by= ('total_value'), ascending= False)
    return combinaciones_sort

#Mandamos llamar la funcion separandola en los dos casos que queremos observar

ruta_exports= rutas(exports)
ruta_imports= rutas(imports)

print(ruta_exports)
print(ruta_imports)


#%% Segundo ejercicio 

#Al igual que en el ejercicio anterior se hace una funcion que combbine los grupos que se necesitan, en este 
# solo son dos, se suma el 'total_vale' tomando como referencia las categorias seleccionadas y se ordenan 
# orden descendente 

def transporte(df):  
    comb_transporte= df.groupby(by=['direction','transport_mode']).sum()['total_value'].reset_index()
    transporte_sort= comb_transporte.sort_values(by= ('total_value'), ascending= False)
    return transporte_sort

#Se manda llamar la función y se imprimen los resultados 
transporte_export= transporte(exports)
transporte_imports= transporte(imports)

print("Las ganancias según el medio de transporte en exportaciones son de:\n ", transporte_export)
print("Las ganancias según el medio de transporte en importaciones son de:\n ", transporte_imports)




#%%Tercer ejercicio 

#Creamos una función para generar una lista de datos donde se puedan observar las
#ganancias por país, su procentaje con respecto al total y su porcentaje acumulado
#primero se define el grupo de referencia que es 'origin' y se suma el 'total_value' 
#para cada elemento de este grupo, posteriormete se hace una pequeña operación para 
#sacar el porcentaje de cada elemento, se ordenan de mayor a menor y por último se utiliza 
#una función para obtener el porcentaje acumulado. Se hace una pequeña condicion 
# para que al momento de sobrepasar el 80% ya no mande más objetos a la lista

def sol_3(df, p):
    valor_pais = df.groupby('origin').sum()['total_value'].reset_index()
    valor_total_porcentaje = valor_pais['total_value'].sum()
    valor_pais['percent'] = 100 * valor_pais['total_value'] / valor_total_porcentaje
    valor_pais.sort_values(by='percent', ascending=False, inplace=True)
    valor_pais['cumsum'] = valor_pais['percent'].cumsum()
    lista_paises = valor_pais[valor_pais['cumsum'] < p]
    return lista_paises


#Se manda llamar la función y se imprimen los resultados 
res = sol_3(exports, 80)
res2= sol_3(imports, 80)

print('Estos son los países que generan el 80% de las ganancias según las exportaciones:\n', res)
print('Estos son los países que generan el 80% de las ganancias según las importaciones:\n', res2)
