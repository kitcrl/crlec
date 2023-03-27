import os;
import numpy as np;
import matplotlib.pyplot as plt;

FONT_SMALL = 8;
FONT_MEDIUM = 10;
FONT_BIG = 24;

ppath = os.getcwd() + "\\imgs\\";
fname = 'figure_1';
_X_ = np.arange(0,20,0.00001);

def f(x) :
  return np.cos(np.tan(x)) + np.log(x);


plt.rc('xtick', labelsize=FONT_BIG);
plt.rc('ytick', labelsize=FONT_BIG);

plt.figure(figsize=(16.5,8.5), dpi=300);
plt.axis( [0, 20, -2, 5] );
plt.plot( _X_, f(_X_), 'r-');


plt.xlabel('x', fontdict={'family':'Courier New', 'weight':'bold', 'style':'italic', 'size':32}, loc='right');
plt.ylabel('f(x)', fontdict={'family':'Courier New', 'weight':'bold', 'style':'italic', 'size':32, 'rotation':'vertical'}, loc='top');

plt.savefig(ppath + fname+'.png');
#plt.show();