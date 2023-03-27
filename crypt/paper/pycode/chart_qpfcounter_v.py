import csv;
import numpy as np;
import matplotlib.pyplot as plt;

FONT_SMALL = 8;
FONT_MEDIUM = 10;
FONT_BIG = 24;

WIDTH = 512;

f = open('c.csv','r');
rdr = csv.reader(f);
values = [];

i = 0;
for line in rdr:
    #print(i , ' -> ', line);
    j = 0;
    for v in line:
        if (j<WIDTH) :
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

plt.figure(figsize=(16.5,7.5));
plt.axis( [0, max, 0, 1200] );


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

plt.xlabel('pixel', fontdict={'family':'Courier New', 'weight':'bold', 'style':'italic', 'size':32}, loc='right');
plt.ylabel('gray scale', fontdict={'family':'Courier New', 'weight':'bold', 'style':'italic', 'size':32, 'rotation':'vertical'}, loc='top');

plt.show();