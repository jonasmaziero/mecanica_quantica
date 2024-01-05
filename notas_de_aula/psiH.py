import numpy as np 
import math 

def psi_H(Z,mu,a0,x,z):
    pi = math.pi 
    return sqrt(2)*x*z*sqrt(Z**3/a0**3)*exp(-x/2)/(8*sqrt(pi))

def sqrt(x):
    return np.sqrt(x) 

def exp(x):
    return np.exp(x) 
