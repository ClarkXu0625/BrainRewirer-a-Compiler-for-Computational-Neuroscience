import numpy as np
import neuron
from brian2 import *


class HHModel:
    """The HHModel tracks conductances of 3 channels to calculate Vm"""

    class Gate:
        """The Gate object manages a channel's kinetics and open state"""
        alpha, beta, state = 0, 0, 0

        def update(self, deltaTms):
            alphaState = self.alpha * (1-self.state)
            betaState = self.beta * self.state
            self.state += deltaTms * (alphaState - betaState)

        def setInfiniteState(self):
            self.state = self.alpha / (self.alpha + self.beta)

    ENa, EK, EKleak = 115, -12, 10.6
    gNa, gK, gKleak = 120, 36, 0.3
    m, n, h = Gate(), Gate(), Gate()
    Cm = 1
    

    def __init__(self, startingVoltage=0):
        self.Vm = startingVoltage
        self._UpdateGateTimeConstants(startingVoltage)
        self.m.setInfiniteState()
        self.n.setInfiniteState()
        self.h.setInfiniteState()

    def _UpdateGateTimeConstants(self, Vm, V_T):
        """Update time constants of all gates based on the given Vm"""
        self.n.alpha = (Vm-V_T-15) * .032/ (np.exp((Vm-V_T-15)/5)-1)
        self.m.alpha = (Vm-V_T-13) * .32/ (np.exp((Vm-V_T-13)/4)-1)
        self.h.alpha = .128*np.exp((Vm-V_T-17)/18)
        
        self.n.beta = .5*np.exp((Vm-V_T-10*mV)/40)
        self.m.beta = .28*np.exp((Vm-V_T-40)/5-1)
        self.h.beta = 4/(np.exp((Vm-V_T-40)/5)+1)
        # self.n.alpha = .01 * ((10-Vm) / (np.exp((10-Vm)/10)-1))
        # self.n.beta = .125*np.exp(-Vm/80)
        # self.m.alpha = .1*((25-Vm) / (np.exp((25-Vm)/10)-1))
        # self.m.beta = 4*np.exp(-Vm/18)
        # self.h.alpha = .07*np.exp(-Vm/20)
        # self.h.beta = 1/(np.exp((30-Vm)/10)+1)

    def _UpdateCellVoltage(self, stimulusCurrent, deltaTms):
        """calculate channel currents using the latest gate time constants"""
        self.INa = np.power(self.m.state, 3) * self.gNa * \
            self.h.state*(self.Vm-self.ENa)
        self.IK = np.power(self.n.state, 4) * self.gK * (self.Vm-self.EK)
        self.IKleak = self.gKleak * (self.Vm-self.EKleak)
        Isum = stimulusCurrent - self.INa - self.IK - self.IKleak
        self.Vm += deltaTms * Isum / self.Cm

    def _UpdateGateStates(self, deltaTms):
        """calculate new channel open states using latest Vm"""
        self.n.update(deltaTms)
        self.m.update(deltaTms)
        self.h.update(deltaTms)

    def iterate(self, stimulusCurrent, deltaTms):
        self._UpdateGateTimeConstants(self.Vm)
        self._UpdateCellVoltage(stimulusCurrent, deltaTms)
        self._UpdateGateStates(deltaTms)