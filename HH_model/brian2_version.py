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