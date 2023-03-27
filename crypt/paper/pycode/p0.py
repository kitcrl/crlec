import numpy as np;
import matplotlib.pyplot as plt;

tan1 = 0;
tan2 = 3;
pox = 1.5;
dx = 0.0000000001;


x1 = np.arange(-50,100,0.0001);

def h(x) :
  return (tan1*(x-pox))+ bias;

def g(x) :
  return (tan2*x) +2;

def f(x) :
  return (x*x);

def df(x, h) :
  return ( (f(x + h) - f(x))/h );

bias = f(pox);
tan1 = df(pox, dx);


y1 = f(x1);
y2 = g(x1);
y3 = h(x1);

plt.axis( [-2, 7, -7, 25] );
plt.plot( x1, y1, 'r-', x1,y2, 'b-', x1, y3, 'g-');

plt.show();