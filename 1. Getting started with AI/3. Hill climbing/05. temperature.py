# Warmp-up exercise for simulated annealing

import random
import numpy as np

def accept_prob(S_old, S_new, T):
    return min(np.exp(-(S_old - S_new) / T), 1.0)


# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)

for i in range(100):
    print(accept_prob(-100, 100, 200))