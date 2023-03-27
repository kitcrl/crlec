import os;
import math;
import numpy as np;
import matplotlib.pyplot as plt;

ppath = os.getcwd() + "\\imgs\\";
fname = 'figure_3';


ROUND_V = 4;
dx = 0.01;

ax = 1.5;
bx = 3.7;

_X_ = np.arange(0,512,0.0001);
poi = [];

FONT_SMALL = 8;
FONT_MEDIUM = 10;
FONT_BIG = 24;

def check_tan(l, t) :
  idx = 0;
  for i in l :
    _t = df(np.round(i, ROUND_V), dx);
    #print(" i -> ", np.round(i, ROUND_V), ", ", np.round(_t, ROUND_V));
    if ( np.round(_t, ROUND_V) == t ) :
      poi.append(np.round(i, ROUND_V));
      idx += 1;
  return idx;

def tnsqre(x) :
  r = 1;
  for i in range(0, x) :
    r *= 10;
  return r;

def h(x, x1) :
  return (tan1*(x-x1) + f(x1));

def g(x) :
  return (tan1*(x-a[0]) + a[1]);

def f(x) :
  return (np.cos(np.tan(x))+np.log(x));

def df(x, h) :
  return ( (f(x + h) - f(x))/h );

a = [ax, f(ax)];
b = [bx, f(bx)];

tan1 = np.round( ((f(b[0])-f(a[0]))/(b[0]-a[0])), ROUND_V);


print("tan1 --> ", tan1);
check_tan(_X_, tan1);





plt.rc('xtick', labelsize=FONT_BIG);
plt.rc('ytick', labelsize=FONT_BIG);

plt.figure(figsize=(16.5,8.5), dpi=300);
plt.axis( [0, 512, -2, 10] );
plt.plot( _X_, f(_X_), 'r-');
plt.plot( _X_, g(_X_), 'b-');# _X_, h(_X_), 'g-');

for i in poi:
  plt.plot( _X_, h(_X_, i), 'g-' );

plt.xlabel('x', fontdict={'family':'Courier New', 'weight':'bold', 'style':'italic', 'size':32}, loc='right');
plt.ylabel('f(x)', fontdict={'family':'Courier New', 'weight':'bold', 'style':'italic', 'size':32, 'rotation':'vertical'}, loc='top');

plt.savefig(ppath + fname+'.png');
#plt.show();