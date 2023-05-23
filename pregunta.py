"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from re import match 
from datetime import datetime

def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df=df.dropna()
    df['sexo'] = df.sexo.str.lower()
    df['tipo_de_emprendimiento'] = df.tipo_de_emprendimiento.str.lower()
    df['idea_negocio']=df['idea_negocio'].apply(lambda x: x.lower().replace("_", " ").replace("-", " "))
    df['barrio']=df['barrio'].apply(lambda x: x.lower().replace("_"," ").replace("-"," "))
    df['línea_credito']=df['línea_credito'].apply(lambda x: x.lower().replace("-"," ").replace("_"," "))
    df['comuna_ciudadano'] = df.comuna_ciudadano.astype(int)
    df['monto_del_credito']=df['monto_del_credito'].apply(lambda x: x.strip("$").replace(",","")).astype(float)
    df['fecha_de_beneficio'] =df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x,"%d/%m/%Y") if match(r"\d{1,2}/\d{2}/\d{4}", x) else datetime.strptime(x,"%Y/%m/%d"))
    df=df.drop_duplicates()
    return df
