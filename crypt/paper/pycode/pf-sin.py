import os;
import numpy as np;
import matplotlib.pyplot as plt;

a = 0.2;
dx = 0.2312;
delta = 1.0;
da = 4;
xrange = 60;
_poi_X_ = [];

FONT_SMALL = 8;
FONT_MEDIUM = 10;
FONT_BIG = 24;

ppath = os.getcwd() + "\\imgs\\";
fname = 'pf_sin.bmp';


_X_ = np.arange(0,da*np.pi,0.0001);
_Y_ = [];

def f(x) :
  return np.sin(x);

def g(x, i) :
    return a + i*dx;

for i in np.arange(0,xrange,delta):
    _poi_X_.append(g(a,i));
    _Y_.append(0);


plt.rc('xtick', labelsize=FONT_BIG);
plt.rc('ytick', labelsize=FONT_BIG);

plt.figure(figsize=(16.5,7.5), dpi=300);
plt.axis( [0, da*np.pi, -1.23, 1.23] );

#plt.plot( _X_, f(_X_), 'r,');
plt.plot(_poi_X_, f(_poi_X_), 'b.');
plt.scatter( _poi_X_, _Y_, s=1, c='#0000FF' );

for i in np.arange(0,xrange,1):
    plt.vlines(_poi_X_[i], 0, f(_poi_X_[i]), color='#00FF00', linestyle='--', linewidth=0.2);
    plt.hlines(f(_poi_X_[i]), 0, _poi_X_[i], color='#999999', linestyle='--', linewidth=0.2);




plt.xlabel('x', fontdict={'family':'Courier New', 'weight':'bold', 'style':'italic', 'size':32}, loc='right');
plt.ylabel('f(x)', fontdict={'family':'Courier New', 'weight':'bold', 'style':'italic', 'size':32, 'rotation':'horizontal'}, loc='top');


plt.savefig(ppath + fname+'1.0.x.y.b.dot.y.v.png');
#plt.show();