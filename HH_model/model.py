import numpy as np
from brian2 import *


class HHModel:
    """The HHModel tracks conductances of 3 channels to calculate Vm"""

    class Gate:
        """The Gate object manages a channel's kinetics and open state"""
        alpha, beta, state = 0, 0, 0

        def update(self, dt):
            alphaState = self.alpha * (1-self.state)
            betaState = self.beta * self.state
            self.state += (alphaState - betaState)*dt

        def setInfiniteState(self):
            # self.state = self.alpha / (self.alpha + self.beta)
            self.state = 0

    ##### unit here
    def __init__(self, group_name, dt, PARAM, startingVoltage=-56.2*mV):
        self.group = group_name
        self.Vm = startingVoltage
        self.dt = dt
        self.load_param(PARAM)
        self.m, self.n, self.h = self.Gate(), self.Gate(), self.Gate()
        self.m.setInfiniteState()
        self.n.setInfiniteState()
        self.h.setInfiniteState()
        self.r = 1
        # self._update_gate_time_constants()

    def load_param(self, P):
        self.model_param(P.C_M, P.V_K, P.V_Ca, P.V_Na, P.V_L, P.V_T, P.g_K_max, 
                        P.g_M_max, P.g_Ca_max, P.g_Na_max, P.g_L, P.tau_max)
        self.synaptic_param(P.tau_r, P.tau_d, P.V_syn, P.V_0)

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
        # remove units for gating variable calculations
        V_T = self.V_T      # * 10**3
        Vm = self.Vm        # * 10**3
        diff = (self.Vm - self.V_T)/mV

        self.n.alpha = (diff-15) * .032/ (np.exp((diff-15)/5)-1)
        self.m.alpha = (diff-13) * .32/ (np.exp((diff-13)/4)-1)
        self.h.alpha = .128*np.exp((diff-17)/18)
        
        self.n.beta = .5*np.exp((diff-10)/40)
        self.m.beta = .28*np.exp((diff-40)/5-1)
        self.h.beta = 4/(np.exp((diff-40)/5)+1)

    def _update_voltage(self, stimulusCurrent):
        """calculate channel currents using the latest gate time constants"""
        pass


    def _update_gate_states(self):
        """calculate new channel open states using latest Vm"""
        self.n.update(self.dt)
        self.m.update(self.dt)
        self.h.update(self.dt)

    def iterate(self, stimulus_current):
        self._update_gate_time_constants()
        self._update_voltage(stimulus_current)
        self._update_gate_states()
    
    def receptor_fraction(self):
        rdt = (1/self.tau_r + 1/self.tau_d)*(1-self.r)
    #def _UpdateGateTimeConstant_m()