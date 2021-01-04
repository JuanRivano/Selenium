#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import buscar_reg_civil
from leer_pdfs import extraer_texto_pdf,ls,extraer_nombre_fecha_nac
from crear_excel_informacion import cargar_valores_en_excel
from api_google import buscar_correo

nombre_fecha=[]
ruts=[]
for rut in ruts:
 buscar_reg_civil.BuscarRegistroCivil(rut)
time.sleep(10)
buscar_correo()
lista_arq = ls('pdf/')
for archivo in lista_arq:
    if archivo[0:3]=="NAC":
        texto=extraer_texto_pdf(archivo)
        nombre_fecha.append(extraer_nombre_fecha_nac(texto))
print(nombre_fecha)
cargar_valores_en_excel(nombre_fecha)