import matplotlib.pyplot as plt
import numpy as np
from main import FS_PARAM, RSA_PARAM, IB_PARAM
from neuron import FS, RSA, IB

dt = 1e-4                               # size of a time step, 0.1ms
simulation_time = 10                    # total seconds of simulation
t = np.arange(0, simulation_time, dt)   # time vector
Nt = t.size                             # number of time steps
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

class PARAM_MATRIX:
    '''store and load param for a neuron network'''

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
        n = a+b+c

NETWORK_PARAM = PARAM_MATRIX(30, 90, 30)
N = len(NETWORK_PARAM.n)                        # size of the network



A_el = np.zeros((N,N))          # adjacency matrix
D = np.zeros((N,N))             # diagonal degree matrix
L = np.zeros((N,N))             # Laplacian matrix, or connectivity matrix
voltage_matrix = np.zeros((Nt, N))



        


def inj_current(V):
    pass
    # TODO: figure out connectivity

'''psudocode for iterate over time time: '''
for i in range(Nt):
    current = inj_current(voltage_matrix[i,:])
    for j in range(n):
        neuron = neuron_list[j]       
        neuron.iterate(current[j])
        voltage_matrix[i,j] = neuron.Vm


