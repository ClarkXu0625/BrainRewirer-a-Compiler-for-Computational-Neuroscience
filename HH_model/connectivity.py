import matplotlib.pyplot as plt
import numpy as np
from main import FS_PARAM, RSA_PARAM, IB_PARAM
from neuron import FS, RSA, IB

dt = 1e-4                               # size of a time step, 0.1ms
simulation_time = 10                    # total seconds of simulation
t = np.arange(0, simulation_time, dt)   # time vector
voltage = np.zeros(t.shape)


neuron_list = []
for i in range(30):
    FS_neuron = FS(dt, FS_PARAM)
    neuron_list.append(FS_neuron)

for i in range(90):
    RSA_neuron = RSA(dt, RSA_PARAM)
    neuron_list.append(RSA_neuron)

for i in range(30):
    IB_neuron = IB(dt, IB_PARAM)
    neuron_list.append(IB_neuron)

