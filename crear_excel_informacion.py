import xlsxwriter

def cargar_valores_en_excel(registros):
    workbook = xlsxwriter.Workbook('pdf\Expenses01.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "Nombre")
    worksheet.write(0, 1 , "Fecha")
    worksheet.write(0, 2 , "Años")
    row = 1
    col = 0
    for registro in (registros):
        nombre,fecha,años=registro.split(":")
        worksheet.write(row, col, nombre)
        worksheet.write(row, col + 1, fecha)
        worksheet.write(row, col + 2,años)
        row += 1
    workbook.close()