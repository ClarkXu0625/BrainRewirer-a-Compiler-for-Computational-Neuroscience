import numpy as np
from neuron import FS, RSA, IB
from brian2 import *
from brian2.units.allunits import *
import matplotlib.pyplot as plt

dt = 1e-4                               # size of a time step, 0.1ms
simulation_time = 10                    # total seconds of simulation
t = np.arange(0, simulation_time, dt)   # time vector
voltage = np.zeros(t.shape)


'''Data structure that contains parameters for each type of neuron in HH model'''
class FS_PARAM:
    # model param
    C_M = 0.5e-6        # 0.5 ufarad/cmeter2
    V_K = -90e-3        # -90 mV
    V_Ca = NaN          # NA
    V_Na = 50e-3        # 50 mV
    V_L = -70e-3        # -70 mV
    V_T = -56.2e-3      # -56.2 mV
    g_K_max = 10e-3     # 10 msiemens/cmeter2
    g_M_max = NaN       # NA
    g_Ca_max = NaN      # NA
    g_Na_max = 56e-3    # 56 msiemens/cmeter2
    g_L = 1.5e-5        # 1.5e-2 msiemens/cmeter2
    tau_max = 1e-3      # 1 ms

    # synapse param
    tau_r = 0.5e-3      # 0.5 ms
    tau_d = 8e-3        # 8 ms
    V_syn = -80e-3      # -80 mV
    V_0 = -20e-3        # -20 mV

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
    

# connectivity = np.array()
FS_neuron = FS(dt, FS_PARAM)
# load_param(FS_neuron, FS_PARAM)
for i in range(t.size):
    FS_neuron.iterate(0)
    voltage[i] = FS_neuron.Vm

print(voltage.shape)
plt.plot(t, voltage)
