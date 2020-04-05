# Program extracting first column 
import xlrd 
  
loc = ("pricelist_29-1-20.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
for i in range(sheet.nrows):
    if i==0:
        continue
    name= sheet.cell_value(i, 0)
    price=str(sheet.cell_value(i, 1))[:-2]
    print('''<button id="{}" onclick="totalprice(this,{})">(0) <span>{}</span><br>Rs. {}</button>'''.format(i,price,name,price))

        
