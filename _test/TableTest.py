# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:09:53 2013

@author: Josh
"""


import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

sys.path.append("..\globales\python")
from latextables import toTable as tab
from latextables_alpha import toTable as tabalpha

a = np.array([1.589, 15.477, 3.789, 9.784, 184.1589746, 31.4])
b = np.array([0.00456, 0.1111234, 123.342, 1.34, 9.0004, 12.1])
c = np.array([789.15, 0.4534442, 234.203, 89.0923, 10.745769])

a_err = np.array([0.046, 0.54, 0.001, 1e-05, 1.4, 4])
b_err = np.array([0.01, 0.002, 1.5, 0.01452, 1.455, 1])

uA = unp.uarray(a, a_err)
uB = unp.uarray(b, b_err)


#print(tabalpha([uA, uB, c],
#          col_titles=["Spannung", "Zeit", "Temperatur"],
#          col_syms=["U", "t", "T"],
#          col_units=["V", "s", r"\kelvin"],
#          fmt=["c", "c", "c"],
#          cap="table to test function toTable",
#          label="Test"))
#
#f = open("Daten/Table.tex", "w")
#
#f.write(tabalpha([uA, uB, c],
#        col_titles=["Spannung", "Zeit", "Temperatur"],
#        col_syms=["U", "t", "T"],
#        col_units=["V", "s", r"\kelvin"],
#        fmt=["c", "c", "c"],
#        cap="table to test function toTable",
#        label="Test"))
#
#f.close()
#


#print(tabalpha([uA[:len(uA)/2:], uB[:len(uB)/2:], uA[len(uA)/2::], uB[len(uB)/2::]],
#          col_titles=["Spannung", "Zeit", "Temperatur"],
#          col_syms=["U", "t", "T"],
#          col_units=["V", "s", r"\kelvin"],
#          fmt=["c", "c", "c"],
#          cap="table to test function toTable",
#          label="Test",
#          doubleTab=True))

f = open("Daten/Table2.tex", "w")

f.write(tabalpha([uA, uB, c],
        col_titles=["Spannung", "Zeit", "Temperatur"],
        col_syms=["U", "t", "T"],
        col_units=["V", "s", r"\kelvin"],
        fmt=["c", "c", "c"],
        cap="table to test function toTable",
        label="Test"))

f.close()

print(tab([uA, uB, c],
        col_titles=["Spannung", "Zeit", "Temperatur"],
        col_syms=["U", "t", "T"],
        col_units=["V", "s", r"\kelvin"],
        fmt=["c", "c", "c"],
        cap="table to test function toTable",
        label="Test"))

#text = ["Spannung", "Zeit", "Temperatur"]
#
#if not isinstance(text, np.ndarray):
#    text = np.array(text)
#print(len(text))
#print(np.where(text == "Temperatur"))
#print((np.where(text == "Temperatur")[0])[0] == (len(text)-1))

