import numpy as np
from neuron import FS, RSA, IB
from brian2 import *
from brian2.units.allunits import *
import matplotlib.pyplot as plt

dt = 1e-4                               # size of a time step, 0.1ms
simulation_time = 10                    # total seconds of simulation
t = np.arange(0, simulation_time, dt)   # time vector
voltage = np.zeros(t.shape)
Nt = t.size


'''Data structure that contains parameters for each type of neuron in HH model'''
class FS_PARAM:
    # model param
    C_M = 0.5 * ufarad/cmeter2          #0.5e-6        # 0.5 * ufarad/cmeter2
    V_K = -90 * mV                      #-90e-3        # -90 * mV
    V_Ca = NaN          # NA
    V_Na = 50 * mV                      #50e-3        # 50 * mV
    V_L = -70 * mV                      #-70e-3        # -70 * mV
    V_T = -56.2 * mV                    #-56.2e-3      # -56.2 * mV
    g_K_max = 10 * msiemens/cmeter2     #10e-3     # 10 * msiemens/cmeter2
    g_M_max = NaN       # NA
    g_Ca_max = NaN      # NA
    g_Na_max = 56 * msiemens/cmeter2    #56e-3    # 56 * msiemens/cmeter2
    g_L = .5e-2 * msiemens/cmeter2      #1.5e-5        # 1.5e-2 * msiemens/cmeter2
    tau_max = 1 * ms                    #1e-3      # 1 * ms

    # synapse param
    tau_r = 0.5 * ms        #0.5e-3      # 0.5 * ms
    tau_d = 8 * ms          #8e-3        # 8 * ms
    V_syn = -80 * mV        #-80e-3      # -80 * mV
    V_0 = -20 * mV          #-20e-3        # -20 * mV

class RSA_PARAM:
    # model param
    C_M = 1e-6          # 1 * ufarad/cmeter2
    V_K = -90e-3        # -90 * mV
    V_Ca = NaN          # NA
    V_Na = 56e-3        # 56 mV
    V_L = -70.3e-3      # -70.3 mV
    V_T = -56.2e-3      # -56.2 mV
    g_K_max = 6e-3      # 6 msiemens/cmeter2
    g_M_max = 0.075e-3  # 0.075 msiemens/cmeter2
    g_Ca_max = NaN      # NA
    g_Na_max = 56e-3    # 56 msiemens/cmeter2
    g_L = 2.05e-5       # 2.05e-2 * msiemens/cmeter2
    tau_max = 608e-3    # 608 * msecond

    # synapse param
    tau_r = 0.5e-3      # 0.5 * msecond
    tau_d = 8e-3        # 8 * msecond
    V_syn = 20e-3       # 20 * mvolt
    V_0 = -20e-3        # -20 * mvolt


class IB_PARAM:
    # model param
    C_M = 1e-6          # 1 * ufarad/cmeter2
    V_K = -90e-3        # -90 * mV
    V_Ca = 120e-3       # 120 *mV
    V_Na = 50e-3        # 50 * mV
    V_L = -70e-3        # -70 * mV
    V_T = -56.2e-3      # -56.2 * mV
    g_K_max = 5e-3      # 5 * msiemens/cmeter2
    g_M_max = 3e-5      # 0.03 * msiemens/cmeter2
    g_Ca_max = 2e-4     # 0.2 * msiemens/cmeter2
    g_Na_max = 50e-3    # 50 * msiemens/cmeter2
    g_L = 1e-5          # 1e-2 * msiemens/cmeter2
    tau_max = 608e-3    # 608 * msecond

    # synapse param
    tau_r = 0.5e-3      # 0.5 * msecond
    tau_d = 8e-3        # 8 * msecond
    V_syn = 20e-3       # 20 * mvolt
    V_0 = -20e-3        # -20 * mvolt


    

if __name__ == '__main__':
    # connectivity = np.array()
    # IB_neuron = IB(dt, IB_PARAM)
    FS_neuron = FS(dt, FS_PARAM)

    #########
    '''model injection current'''
    a = 1
    b = 10
    d = 5
    l = int(Nt/d)
    ##########

    for i in range(Nt):
        FS_neuron.iterate(0)
        voltage[i] = FS_neuron.Vm

    voltage = voltage*1000
    #print(voltage.shape)
    plt.plot(t, voltage)
    plt.show()


