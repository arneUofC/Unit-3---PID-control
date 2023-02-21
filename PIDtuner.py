import numpy as np
from matplotlib import pyplot as plt
import control as ct
import enel441_utilities as eu


#plt.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True

#def mouse_event(event):
#   print('x: {} and y: {}'.format(event.xdata, event.ydata))
#   PID_zeros = np.array([complex(event.xdata, event.ydata), complex(event.xdata, -event.ydata)])
#   PID_zeros_num = eu.roots_to_polynomial(PID_zeros)
#   L = ct.tf(np.convolve(P_num,PID_zeros_num),np.convolve([1, 0], P_den))
#   ct.root_locus(L,ax=ax)


#fig, ax = plt.subplots(1)
#cid = fig.canvas.mpl_connect('button_press_event', mouse_event)

P_num = 1
P_den = [1, 2, 2]
P = ct.tf(P_num,P_den)

#cl_poles, K = ct.root_locus(P, ax=ax)

#ct.rootlocus_pid_designer(P)

ct.sisotool(P)

plt.show()