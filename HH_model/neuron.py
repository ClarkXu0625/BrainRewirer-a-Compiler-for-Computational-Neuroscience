from brian2 import *
import numpy as np
from model import HHModel


class FS(HHModel):
    def __init__(self):
        super.__init__('FS')
        super.synaptic_param()
        super.model_param()

    def updata_voltage(self, Vm, n, m, h, I_inj):
        dVdt = (1/self.C_m)*(I_inj - self.g_K_max*(n**4)*(Vm-self.V_K) - self.g_Na_max*(m**3)*h*(Vm-self.V_Na) - self.g_L*(Vm-self.V_L))
        return Vm+dVdt
    


class RSA(HHModel):
    def __init__(self):
        super.__init__()


class IB(HHModel):
    def __init__(self):
        super().__init__()