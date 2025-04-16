def wf(alpha,u,n):
    from math import exp,sqrt,pi 
    return sqrt(715)*alpha**(1/4)*u*(128*u**14 - 6720*u**12 + 131040*u**10 - 1201200*u**8 + 5405400*u**6 - 11351340*u**4 + 9459450*u**2 - 2027025)*exp(-u**2/2)/(21621600*pi**(1/4))