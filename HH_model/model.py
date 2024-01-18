import numpy as np
from brian2 import *



class HHModel:
    """The HHModel tracks conductances of 3 channels to calculate Vm"""

    class Gate:
        """The Gate object manages a channel's kinetics and open state"""
        alpha, beta, state = 0, 0, 0

        def update(self):
            alphaState = self.alpha * (1-self.state)
            betaState = self.beta * self.state
            self.state += alphaState - betaState

        def setInfiniteState(self):
            self.state = self.alpha / (self.alpha + self.beta)


    def __init__(self, group_name, startingVoltage):
        self.group = group_name
        self.Vm = startingVoltage
        self._update_gate_time_constants(startingVoltage)
        self.m, self.n, self.h = self.Gate(), self.Gate(), self.Gate()
        self.m.setInfiniteState()
        self.n.setInfiniteState()
        self.h.setInfiniteState()

    def synaptic_param(self, tau_r, tau_d, V_syn, V_0):
        # set up synaptic parameter
        self.tau_r = tau_r
        self.tau_d = tau_d
        self.V_syn = V_syn
        self.V_0 = V_0
        
    def model_param(self, C_m, V_K, V_Ca, V_Na, V_L, V_T, g_K_max, g_M_max, g_Ca_max, g_Na_max, g_L, tau_max):
        # set up model parameters
        self.C_m = C_m              # membrane charge
        self.V_K = V_K              # potassium nernst voltage
        self.V_Ca = V_Ca            # calcium nernst voltage
        self.V_Na = V_Na            # sodium nernst voltage
        self.V_L = V_L              # leaky nernst voltage
        self.V_T = V_T              # threshold adjustment constant
        self.g_K_max = g_K_max
        self.g_M_max = g_M_max
        self.g_Ca_max = g_Ca_max
        self.g_Na_max = g_Na_max
        self.g_L = g_L
        self.tau_max = tau_max
        

    def _update_gate_time_constants(self):
        """Update time constants of all gates based on the given Vm"""
        V_T = self.V_T
        Vm = self.Vm

        self.n.alpha = (Vm-V_T-15) * .032/ (np.exp((Vm-V_T-15)/5)-1)
        self.m.alpha = (Vm-V_T-13) * .32/ (np.exp((Vm-V_T-13)/4)-1)
        self.h.alpha = .128*np.exp((Vm-V_T-17)/18)
        
        self.n.beta = .5*np.exp((Vm-V_T-10*mV)/40)
        self.m.beta = .28*np.exp((Vm-V_T-40)/5-1)
        self.h.beta = 4/(np.exp((Vm-V_T-40)/5)+1)

    def _update_voltage(self, stimulusCurrent):
        """calculate channel currents using the latest gate time constants"""
        pass


    def _update_gate_states(self):
        """calculate new channel open states using latest Vm"""
        self.n.update()
        self.m.update()
        self.h.update()

    def iterate(self, stimulus_current):
        self._update_gate_time_constants()
        self._update_voltage(stimulus_current)
        self._update_gate_states()
    
    #def _UpdateGateTimeConstant_m()