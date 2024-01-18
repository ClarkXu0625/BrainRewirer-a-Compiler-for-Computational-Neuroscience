from brian2 import *
import numpy as np
from model import HHModel


class FS(HHModel):
    def __init__(self, dt):
        super().__init__('FS', dt)
        

    def _update_voltage(self, I_inj):
        Vm = self.Vm
        m, n, h = self.m.state, self.n.state, self.h.state
        dVdt = (1/self.C_m)*(I_inj - self.g_K_max*(n**4)*(Vm-self.V_K) 
                             - self.g_Na_max*(m**3)*h*(Vm-self.V_Na) 
                             - self.g_L*(Vm-self.V_L))
        self.Vm += dVdt*self.dt
    


class RSA(HHModel):
    def __init__(self, dt):
        super().__init__("RSA", dt)
        self.p = 0

    def _update_p(self):
        Vm =self.Vm/mvolt  # remove unit
        p_inf = 1/(np.exp((-Vm-35)/10)+1)
        tau_p = self.tau_max/(3.3*np.exp((Vm+35)/20) + np.exp((-Vm-35)/20))
        dpdt = (p_inf - self.p)/tau_p
        self.p += dpdt*self.dt

    def _update_voltage(self, I_inj):
        Vm = self.Vm
        m, n, h = self.m.state, self.n.state, self.h.state
        dVdt = (1/self.C_m)*(I_inj - self.g_K_max*(n**4)*(Vm-self.V_K) 
                            - self.g_M_max*self.p*(Vm-self.V_K)
                            - self.g_Na_max*(m**3)*h*(Vm-self.V_Na) 
                            - self.g_L*(Vm-self.V_L))
        self.Vm += dVdt*self.dt

    def _update_gate_states(self):
        '''Different from FS, RSA also needs to update variable p'''
        super._update_gate_states()
        self.updata_p()

class IB(HHModel):
    def __init__(self, dt):
        super().__init__("IB", dt)
        self.p = 0
        self.q, self.s = super.Gate(), super.Gate()     # two additional calcium gating variable
        self.q.setInfiniteState()
        self.s.setInfiniteState()

    def _update_p(self):
        Vm = self.Vm/mvolt  # remove unit
        p_inf = 1/(np.exp((-Vm-35)/10)+1)
        tau_p = self.tau_max/(3.3*np.exp((Vm+35)/20) + np.exp((-Vm-35)/20))
        dpdt = (p_inf - self.p)/tau_p
        self.p += dpdt*self.dt

    def _update_gate_time_constants(self):
        '''IB neurons have two more gating variables: q and s'''
        super._update_gate_time_constants()
        Vm = self.Vm
        self.q.alpha = .0055*(-27-Vm)/(np.exp((-27-Vm)/3.8)-1)
        self.s.alpha = .000457*np.exp((-13-Vm)/50)
        self.s.beta = .0065/(np.exp((-15-Vm)/28)+1)
        self.q.beta = .94*np.exp((-75-Vm)/17)

    def _update_voltage(self, I_inj):
        Vm = self.Vm
        m, n, h, q, s = self.m.state, self.n.state, self.h.state, self.q.state, self.s.state
        dVdt = (1/self.C_m)*(I_inj - self.g_K_max*(n**4)*(Vm-self.V_K) 
                            - self.g_M_max*self.p*(Vm-self.V_K)
                            - self.g_Ca_max*(q**2)*s*(Vm-self.V_Ca)
                            - self.g_Na_max*(m**3)*h*(Vm-self.V_Na) 
                            - self.g_L*(Vm-self.V_L))
        self.Vm +=dVdt*self.dt
    
    def _update_gate_states(self):
        '''IB neurons also needs to update variable p, calcium gating variable q and s'''
        super._update_gate_states()
        self.updata_p()
        self.q.update()
        self.s.update()
