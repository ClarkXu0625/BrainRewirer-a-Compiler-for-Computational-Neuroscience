from brian2 import *
import numpy as np

# base classs
class neuron:
    def __init__(self, group_name):
        self.group = group_name

    def synaptic_param(self, tau_r, tau_d, V_syn, V_0):
        # set up synaptic parameter
        self.tau_r = tau_r
        self.tau_d = tau_d
        self.V_syn = V_syn
        self.V_0 = V_0


    def model_param(self, C_m, V_K, V_Ca, V_Na, V_L, V_T, g_K_max, g_M_max, g_Na_max, g_L, tau_max):
        # set up model parameters
        self.C_m = C_m              # membrane charge
        self.V_K = V_K              # potassium nernst voltage
        self.V_Ca = V_Ca            # calcium nernst voltage
        self.V_Na = V_Na            # sodium nernst voltage
        self.V_L = V_L              # leaky nernst voltage
        self.V_T = V_T              # threshold adjustment constant
        self.g_K_max = g_K_max
        self.g_M_max = g_M_max
        self.g_Na_max = g_Na_max
        self.g_L = g_L
        self.tau_max = tau_max



class FS(neuron):
    def __init__(self):
        super.__init__('FS')
        super.synaptic_param()
        super.model_param()


class RSA(neuron):
    def __init__(self):
        super.__init__()


class IB(neuron):
    def __init__(self):
        super().__init__()