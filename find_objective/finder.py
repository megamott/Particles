import openpyxl as op
import numpy as np

table = op.load_workbook(filename="Table.xlsx", data_only=True)

sheet = table['Таблица 2']

column_a = sheet['A']
column_d = sheet['D']
column_e = sheet['E']
column_f = sheet['F']
names = []
d = []
e = []
f = []


def fun(column, arr):
    i = 0
    for sh in column:
        i += 1
        if i > 4:
            arr.append(sh.value)
    return arr


def convert_to_float(arr):
    arr = np.array(arr)
    arr = list(arr.astype(np.float))
    return arr


names = fun(column_a, names)
d = fun(column_d, d)
e = fun(column_e, e)
f = fun(column_f, f)

print(names)
print(d)
print(e)
print(f)

values = []


def make_float(num):
    num = num.replace(' ', '').replace(',', '.').replace("–", "-").replace("I", "1")
    return float(num)


for i in range(len(names)):
    if d[i] is None:
        pass
    else:
        if e[i] == 0:
            pass
        else:
            k = make_float(d[i]) + (0.969) * (make_float(e[i]) - make_float(d[i])) + 0.5 * (0.969) * (0.969 - 1) \
                * ((make_float(f[i]) - make_float(e[i])) - (make_float(e[i]) - make_float(d[i])))
            print("answer: " + str(k) + " " + str(make_float(d[i])) + " " + str(make_float(e[i])) + " " + str(
                make_float(f[i])) + " ")
            values.append(k)

print(values)
print(sorted(values))
