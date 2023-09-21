import numpy as np
import sympy as sym

x = sym.Symbol('x',real=True)

def legendre(n,x):
    y = (x**2 - 1)**n
    poly = sym.diff(y,x,n)/(2**n*np.math.factorial(n))
    return poly

print(legendre(2,x))




def GetWeights(Roots,DLegendre):
    
    Dpoly = sym.lambdify([x],DLegendre[n],'numpy')
    Weights = 2/((1-Roots**2)*Dpoly(Roots)**2)
    
    return Weights


'''
def pesos_legendre(n):
  
  pesos = np.array(np.zeros(n))
  print(pesos)

  for i in range(0,n):
    c_k = 2/((1-x_k**2)*(Pn_prima(x_k))**2)
  return pesos  
'''
print(1+1)