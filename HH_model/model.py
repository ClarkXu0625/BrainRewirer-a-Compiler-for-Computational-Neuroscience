import numpy as np
from brian2 import *


class HHModel:
    """The HHModel tracks conductances of 3 channels to calculate Vm"""



    # m, n, h = Gate(), Gate(), Gate()


    def __init__(self, group_name, startingVoltage):
        self.group = group_name
        self.Vm = startingVoltage
        self._UpdateGateTimeConstants(startingVoltage)
        # self.m.setInfiniteState()
        # self.n.setInfiniteState()
        # self.h.setInfiniteState()

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
        

    def _UpdateGateTimeConstants(self, Vm, V_T):
        """Update time constants of all gates based on the given Vm"""

        self.n.alpha = (Vm-V_T-15) * .032/ (np.exp((Vm-V_T-15)/5)-1)
        self.m.alpha = (Vm-V_T-13) * .32/ (np.exp((Vm-V_T-13)/4)-1)
        self.h.alpha = .128*np.exp((Vm-V_T-17)/18)
        
        self.n.beta = .5*np.exp((Vm-V_T-10*mV)/40)
        self.m.beta = .28*np.exp((Vm-V_T-40)/5-1)
        self.h.beta = 4/(np.exp((Vm-V_T-40)/5)+1)

    def _UpdateCellVoltage(self, stimulusCurrent, deltaTms):
        """calculate channel currents using the latest gate time constants"""
        pass
        # self.INa = np.power(self.m.state, 3) * self.gNa * \
        #     self.h.state*(self.Vm-self.ENa)
        # self.IK = np.power(self.n.state, 4) * self.gK * (self.Vm-self.EK)
        # self.IKleak = self.gKleak * (self.Vm-self.EKleak)
        # Isum = stimulusCurrent - self.INa - self.IK - self.IKleak
        # self.Vm += deltaTms * Isum / self.Cm

    def _UpdateGateStates(self, deltaTms):
        """calculate new channel open states using latest Vm"""
        pass
        # self.n.update(deltaTms)
        # self.m.update(deltaTms)
        # self.h.update(deltaTms)

    def iterate(self, stimulusCurrent, deltaTms):
        pass
        # self._UpdateGateTimeConstants(self.Vm)
        # self._UpdateCellVoltage(stimulusCurrent, deltaTms)
        # self._UpdateGateStates(deltaTms)
    
    #def _UpdateGateTimeConstant_m()