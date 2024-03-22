import numpy as np 
import math 

def psi_H(Z,mu,a0,x,z):
    pi = math.pi 
    return x**3*sqrt(Z**3/a0**3)*(1 - z**2)**1.5*exp(-x/2)/(768*sqrt(pi))

def sqrt(x):
    return np.sqrt(x) 

def exp(x):
    return np.exp(x) 
