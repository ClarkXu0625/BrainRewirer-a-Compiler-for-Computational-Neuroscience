from brian2 import *
from brian2.units.allunits import *
from matplotlib import pyplot as plt

start_scope()

# model param
C_M = 1 * ufarad/cmeter2
V_K = -90 * mV
V_Ca = 120 *mV
V_Na = 50 * mV
V_L = -70 * mV
V_T = -56.2 * mV
g_K_max = 5 * msiemens/cmeter2
g_M_max = 0.03 * msiemens/cmeter2
g_Ca_max = 0.2 * msiemens/cmeter2
g_Na_max = 50 * msiemens/cmeter2
g_L = 1e-2 * msiemens/cmeter2
tau_max = 608 * msecond

# synapse param
tau_r = 0.5 * msecond
tau_d = 8 * msecond
V_syn = 20 * mvolt
V_0 = -20 * mvolt


eqs_HH = '''
dv/dt = (gl*(El-v) - g_na*(m*m*m)*h*(v-ENa) - g_kd*(n*n*n*n)*(v-EK) + I)/Cm : volt
dm/dt = 0.32*(mV**-1)*(13.*mV-v+VT)/
    (exp((13.*mV-v+VT)/(4.*mV))-1.)/ms*(1-m)-0.28*(mV**-1)*(v-VT-40.*mV)/
    (exp((v-VT-40.*mV)/(5.*mV))-1.)/ms*m : 1
dn/dt = 0.032*(mV**-1)*(15.*mV-v+VT)/
    (exp((15.*mV-v+VT)/(5.*mV))-1.)/ms*(1.-n)-.5*exp((10.*mV-v+VT)/(40.*mV))/ms*n : 1
dh/dt = 0.128*exp((17.*mV-v+VT)/(18.*mV))/ms*(1.-h)-4./(1+exp((40.*mV-v+VT)/(5.*mV)))/ms*h : 1
I : amp
'''


tau = 10*ms
eqs = '''
dv/dt = (1-v)/tau : 1
'''