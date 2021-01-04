from os import getcwd, scandir
from PyPDF2 import PdfFileReader
from datetime import date

def extraer_texto_pdf(archivo):
    file=f"pdf/{archivo}"
    pdf=PdfFileReader(file)
    pageObj = pdf.getPage(0)
    text = pageObj.extractText()
    return text

def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]


def extraer_nombre_fecha_nac(text):
    posicion_incial_nombre=text.find("Nombre inscrito")+25
    posicion_final_nombre=text.find("R.U.N")
    nombre=text[posicion_incial_nombre:posicion_final_nombre]
    posicion_incial_fecha=text.find("Fecha nacimiento")+25
    posicion_final_fecha = text.find("Sexo")
    fecha_nacimiento = text[posicion_incial_fecha:posicion_final_fecha]
    fecha_format=formato_fecha_nacimiento(fecha_nacimiento)
    return f"{nombre}:{fecha_nacimiento}:{fecha_format}"

def days_between(d1, d2):
    return abs(d2 - d1).days

def formato_fecha_nacimiento(fecha_nac):
     meses={'Enero':1,'Febrero':2,'Marzo':3,'Abril':4,'Mayo':5,'Junio':6,'Julio':7,'Agosto':8,'Septiembre':9,'Octubre':10,'Noviembre':11,'Diciembre':12}
     dia=fecha_nac[0:2]
     mes=fecha_nac[3:-4]
     año=fecha_nac[-4:]
     d1 = date(int(año), int(meses[mes.strip()]), int(dia))
     d2 = date.today()
     return (int(days_between(d2, d1) / 365))



