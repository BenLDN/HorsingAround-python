from openpyxl import *
from os import walk

path = r'C:\Users\bencekulcsar\Desktop\XLS\\'

sum_counter = 1
first_file=True
wb_sum = Workbook()
ws_sum = wb_sum.active
ws_sum.title="BudgetAll"

file_list=[]

for (dp, dn, fn) in walk(path):
    file_list.extend(fn)
    break
try:
    file_list.remove('BudgetSummary.xlsx')
except ValueError:
    pass

total_files=len(file_list)
done=0

for file in file_list:
    wb_tmp=load_workbook(path + file, data_only=True)
    ws_tmp=wb_tmp["Input Sheet"]
    start_row=4

    if first_file==True:
        first_file=False
        start_row=3
    
    for line in range(start_row, len(ws_tmp['H'])+1):
    
        ws_sum.cell(row=sum_counter,column=1).value=ws_tmp.cell(row=line,column=3).value
        ws_sum.cell(row=sum_counter,column=2).value=ws_tmp.cell(row=line,column=5).value
        ws_sum.cell(row=sum_counter,column=3).value=ws_tmp.cell(row=line,column=6).value
        ws_sum.cell(row=sum_counter,column=4).value=ws_tmp.cell(row=line,column=7).value
        ws_sum.cell(row=sum_counter,column=5).value=ws_tmp.cell(row=line,column=8).value

        ws_sum.cell(row=sum_counter,column=6).value=ws_tmp.cell(row=line,column=16).value
        ws_sum.cell(row=sum_counter,column=7).value=ws_tmp.cell(row=line,column=17).value
        ws_sum.cell(row=sum_counter,column=8).value=ws_tmp.cell(row=line,column=18).value
        ws_sum.cell(row=sum_counter,column=9).value=ws_tmp.cell(row=line,column=19).value
        ws_sum.cell(row=sum_counter,column=10).value=ws_tmp.cell(row=line,column=20).value
        ws_sum.cell(row=sum_counter,column=11).value=ws_tmp.cell(row=line,column=21).value
        ws_sum.cell(row=sum_counter,column=12).value=ws_tmp.cell(row=line,column=22).value
        ws_sum.cell(row=sum_counter,column=13).value=ws_tmp.cell(row=line,column=23).value
        ws_sum.cell(row=sum_counter,column=14).value=ws_tmp.cell(row=line,column=24).value
        ws_sum.cell(row=sum_counter,column=15).value=ws_tmp.cell(row=line,column=25).value
        ws_sum.cell(row=sum_counter,column=16).value=ws_tmp.cell(row=line,column=26).value
        ws_sum.cell(row=sum_counter,column=17).value=ws_tmp.cell(row=line,column=27).value
        
        sum_counter+=1

    done+=1
    print(str(done) + " of " + str(total_files) + " done.")


wb_sum.save(path + "BudgetSummary.xlsx")
