from brian2 import *
import numpy as np
from model import HHModel

class Gate:
    """The Gate object manages a channel's kinetics and open state"""
    alpha, beta, state = 0, 0, 0

    def update(self, deltaTms):
        alphaState = self.alpha * (1-self.state)
        betaState = self.beta * self.state
        self.state += deltaTms * (alphaState - betaState)

    def setInfiniteState(self):
        self.state = self.alpha / (self.alpha + self.beta)


class FS(HHModel):
    def __init__(self):
        super.__init__('FS')
        self.m, self.n, self.h = Gate(), Gate(), Gate()

    def updata_voltage(self, Vm, I_inj):
        m, n, h = self.m.state, self.n.state, self.h.state
        dVdt = (1/self.C_m)*(I_inj - self.g_K_max*(n**4)*(Vm-self.V_K) 
                             - self.g_Na_max*(m**3)*h*(Vm-self.V_Na) 
                             - self.g_L*(Vm-self.V_L))
        return Vm+dVdt
    


class RSA(HHModel):
    def __init__(self):
        super.__init__("RSA")
        self.m, self.n, self.h = Gate(), Gate(), Gate()
        self.p = 0

    def update_p(self, Vm):
        p_inf = 1/(np.exp((-Vm-335)/10)+1)
        tau_p = self.tau_max/(3.3*np.exp((Vm+35)/20) + np.exp((-Vm-35)/20))
        dpdt = (p_inf - self.p)/tau_p
        self.p += dpdt

    def updata_voltage(self, Vm, I_inj):
        m, n, h = self.m.state, self.n.state, self.h.state
        dVdt = (1/self.C_m)*(I_inj - self.g_K_max*(n**4)*(Vm-self.V_K) 
                            - self.g_M_max*self.p*(Vm-self.V_K)
                            - self.g_Na_max*(m**3)*h*(Vm-self.V_Na) 
                            - self.g_L*(Vm-self.V_L))
        return Vm+dVdt


class IB(HHModel):
    def __init__(self):
        super().__init__("IB")
        self.m, self.n, self.h, self.q, self.s= Gate(), Gate(), Gate(), Gate(), Gate()

    def update_p(self, Vm):
        p_inf = 1/(np.exp((-Vm-335)/10)+1)
        tau_p = self.tau_max/(3.3*np.exp((Vm+35)/20) + np.exp((-Vm-35)/20))
        dpdt = (p_inf - self.p)/tau_p
        self.p += dpdt

    def _UpdateGateTimeConstants(self, Vm, V_T):
        '''IB neurons have two more gating variables: q and s'''
        super._UpdateGateTimeConstants(Vm, V_T)
        self.q.alpha = .0055*(-27-Vm)/(np.exp((-27-Vm)/3.8)-1)
        self.s.alpha = .000457*np.exp((-13-Vm)/50)
        self.s.beta = .0065/(np.exp((-15-Vm)/28)+1)
        self.q.beta = .94*np.exp((-75-Vm)/17)

    def updata_voltage(self, Vm, I_inj):
        m, n, h, q, s = self.m.state, self.n.state, self.h.state, self.q.state, self.s.state
        dVdt = (1/self.C_m)*(I_inj - self.g_K_max*(n**4)*(Vm-self.V_K) 
                            - self.g_M_max*self.p*(Vm-self.V_K)
                            - self.g_Ca_max*(q**2)*s*(Vm-self.V_Ca)
                            - self.g_Na_max*(m**3)*h*(Vm-self.V_Na) 
                            - self.g_L*(Vm-self.V_L))
        return Vm+dVdt
