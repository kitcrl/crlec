import os;
import csv;
import numpy as np;
import matplotlib.pyplot as plt;

FONT_SMALL = 8;
FONT_MEDIUM = 10;
FONT_BIG = 24;

WDTH = 1000;
HGHT = 663;


fnames = [
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
'pf_freq_d_05.00.bmp.csv',
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


    print("plotting...");

    plt.rc('xtick', labelsize=FONT_BIG);
    plt.rc('ytick', labelsize=FONT_BIG);

    max = 256;
    _X_ = np.array(range(0,max));

    plt.figure(figsize=(16.5,8.5), dpi=300);
    plt.axis( [0, max, 2300, 2900] );


    _Y_ = [0]*max;
    i = 0;
    for v in values:
        _Y_[v] = _Y_[v] + 1;

    #for arr in enumerate(values):
        #print(_X_, ",", arr[1]);
        #print(arr[1]);
        #plt.plot(_X_, arr[1], 'r-');

    print(_Y_);

    plt.plot( _X_, _Y_, 'r.');

    plt.xlabel('Gray scale', fontdict={'family':'Courier New', 'weight':'bold', 'style':'italic', 'size':32}, loc='right');
    plt.ylabel('Frequency', fontdict={'family':'Courier New', 'weight':'bold', 'style':'italic', 'size':32, 'rotation':'vertical'}, loc='top');

    #plt.show();
    plt.savefig(ppath + fname+'.v0.png');