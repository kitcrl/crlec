import os;
import csv;
import numpy as np;
import matplotlib.pyplot as plt;
import statistics as stat;

FONT_SMALL = 8;
FONT_MEDIUM = 10;
FONT_BIG = 24;

WDTH = 1000;
HGHT = 663;




fnamesx = [
'pf_freq_d_00.00.bmp.csv',
'pf_freq_d_00.50.bmp.csv',
'pf_freq_d_01.00.bmp.csv',
'pf_freq_d_01.50.bmp.csv',
'pf_freq_d_02.00.bmp.csv',
'pf_freq_d_02.50.bmp.csv',
'pf_freq_d_03.00.bmp.csv',
'pf_freq_d_03.50.bmp.csv',
'pf_freq_d_04.00.bmp.csv',
'pf_freq_d_04.50.bmp.csv',
'pf_freq_d_05.00.bmp.csv'];

fnames = [
'pf_sin_d_00.50.bmp.csv',
'pf_sin_d_01.00.bmp.csv',
'pf_sin_d_01.50.bmp.csv',
'pf_sin_d_02.00.bmp.csv',
'pf_sin_d_02.50.bmp.csv',
'pf_sin_d_03.00.bmp.csv',
'pf_sin_d_03.50.bmp.csv',
'pf_sin_d_04.00.bmp.csv',
'pf_sin_d_04.50.bmp.csv',
'pf_sin_d_05.00.bmp.csv']


'''
fnames = [
'pf_systm_d_00.50.bmp.csv',
'pf_systm_d_01.00.bmp.csv',
'pf_systm_d_01.50.bmp.csv',
'pf_systm_d_02.00.bmp.csv',
'pf_systm_d_02.50.bmp.csv',
'pf_systm_d_03.00.bmp.csv',
'pf_systm_d_03.50.bmp.csv',
'pf_systm_d_04.00.bmp.csv',
'pf_systm_d_04.50.bmp.csv',
'pf_systm_d_05.00.bmp.csv']
'''


ppath = os.getcwd() + "\\imgs\\";

for fname in fnames:
    f = open(ppath + fname,'r');
    rdr = csv.reader(f);
    values = [];

    i = 0;
    for line in rdr:
        #print(i , ' -> ', line);
        j = 0;
        for v in line:
            if (j<WDTH) :
                #print(i, ",", j, " -> ", v);
                values.append(int(v));
                #print(i, ",", j, "->", values[i][j]);
            j = j+1;
        #print("----------------------");
        i = i+1;

    f.close();

    max = WDTH*HGHT;
    _X_ = np.array(range(0,max));

    print( np.mean(values), " -> ", np.median(values) , " -> ", stat.mode(values));


