import numpy as np
from neuron import FS, RSA, IB
from brian2 import *
from brian2.units.allunits import *

dt = 1e-4                               # size of a time step
simulation_time = 10                    # total seconds of simulation
t = np.arange(0, simulation_time, dt)   # time vector


'''Data structure that contains parameters for each type of neuron in HH model'''
class FS_PARAM:
    # model param
    C_M = 0.5 * ufarad/cmeter2
    V_K = -90 * mV
    V_Ca = NaN
    V_Na = 50 * mV
    V_L = -70 * mV
    V_T = -56.2 * mV
    g_K_max = 10 * msiemens/cmeter2
    g_M_max = NaN
    g_Ca_max = NaN
    g_Na_max = 56 * msiemens/cmeter2
    g_L = 1.5e-2 * msiemens/cmeter2
    tau_max = 1 * msecond

    # synapse param
    tau_r = 0.5 * msecond
    tau_d = 8 * msecond
    V_syn = -80 * mvolt
    V_0 = -20 * mvolt

class RSA_PARAM:
    # model param
    C_M = 1 * ufarad/cmeter2
    V_K = -90 * mV
    V_Ca = NaN
    V_Na = 56 * mV
    V_L = -70.3 * mV
    V_T = -56.2 * mV
    g_K_max = 6 * msiemens/cmeter2
    g_M_max = 0.075 * msiemens/cmeter2
    g_Ca_max = NaN
    g_Na_max = 56 * msiemens/cmeter2
    g_L = 2.05e-2 * msiemens/cmeter2
    tau_max = 608 * msecond

    # synapse param
    tau_r = 0.5 * msecond
    tau_d = 8 * msecond
    V_syn = 20 * mvolt
    V_0 = -20 * mvolt


class IB_PARAM:
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

def load_param(neuron, P):
    neuron.model_param(P.C_M, P.V_K, P.V_Ca, P.V_Na, P.V_L, P.V_T, P.g_K_max, 
                       P.g_M_max, P.g_Ca_max, P.g_Na_max, P.g_L, p.tau_max)
    neuron.synaptic_param(P.tau_r, P.tau_d, P.V_syn, P.V_0)
    
FS_neuron = FS("FS", dt)
load_param(FS_neuron, FS_PARAM)
for i in t:
    FS_neuron.iterate(0)

