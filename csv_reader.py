#!/usr/bin/env python3.6

import re
import xlwt
from xlwt import Workbook

a = 0
# Workbook is created
wb = Workbook()
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
fh = open('dashboard_monthly_feb19.csv')
for line in fh:
    l = line.strip()
    if a == 0:
        a = a + 1
        continue
    l = l.replace(',', '')
    out = re.split(r'\t+', l)
    print(out[1],out[2])

    sheet1.write(a, 0, out[1].replace('"', ''))
    sheet1.write(a, 1, out[2])
    wb.save('formatted_dash_feb19.xls')
    a = a + 1

fh.close()
