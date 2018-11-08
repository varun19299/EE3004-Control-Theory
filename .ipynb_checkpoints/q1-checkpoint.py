import numpy as np 
import control
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

def get_params(Mp,ts):
    '''
    Mp in percent
    '''

    x = np.log(Mp/100)**2
    zeta = x / (x + np.pi**2)
    zeta = np.sqrt(zeta)

    wn = 4/ts/zeta 

    return zeta, wn

def get_poles(zeta,wn):
    return (complex(-zeta*wn, wn*np.sqrt(1-zeta**2)), complex(-zeta*wn ,- wn*np.sqrt(1-zeta**2)))

zeta, wn = get_params(17,3)
print(f"Zeta {zeta} wn {wn}")

p1, p2 = get_poles(zeta,wn)
print(f"Pole1 {p1} Pole 2 {p2}")

# Plot original root locus
org_sys = control.TransferFunction(1,[1,1,0])
control.root_locus(org_sys)
