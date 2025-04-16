import numpy as np 
import math 

def psi_R(Z,mu,a0,x):
    return sqrt(6)*x*sqrt(Z**3/a0**3)*exp(-x/2)/12

def sqrt(x):
    return np.sqrt(x) 

def exp(x):
    return np.exp(x) 
