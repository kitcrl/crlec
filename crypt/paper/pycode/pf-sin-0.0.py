import numpy as np;
import matplotlib.pyplot as plt;

a = 0.2;
dx = 0.2312;
delta = 0.5;
_poi_X_ = [];

FONT_SMALL = 8;
FONT_MEDIUM = 10;
FONT_BIG = 24;

_X_ = np.arange(0,8*np.pi,0.0001);

def f(x) :
  return np.sin(x);

def g(x, i) :
    return a + i*dx;

for i in np.arange(0,120,delta):
    _poi_X_.append(g(a,i));


plt.rc('xtick', labelsize=FONT_BIG);
plt.rc('ytick', labelsize=FONT_BIG);

plt.figure(figsize=(16.5,7.5));
plt.axis( [0, 8*np.pi, -1.5, 1.5] );
#plt.plot( _X_, f(_X_), 'r-');
plt.plot(_poi_X_, f(_poi_X_), 'b^');
plt.xlabel('x', fontdict={'family':'Courier New', 'weight':'bold', 'style':'italic', 'size':32}, loc='right');
plt.ylabel('f(x)', fontdict={'family':'Courier New', 'weight':'bold', 'style':'italic', 'size':32, 'rotation':'horizontal'}, loc='top');

plt.show();