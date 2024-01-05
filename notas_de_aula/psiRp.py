import numpy as np 
import math 

def psi_R(Z,mu,a0,x):
    return sqrt(2)*sqrt(Z**3/a0**3)*(2 - x)*exp(-x/2)/4

def sqrt(x):
    return np.sqrt(x) 

def exp(x):
    return np.exp(x) 
