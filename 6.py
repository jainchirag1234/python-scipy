# import scipy as sp
# import numpy as np
#
# from scipy.fft import fft
#
# var1=np.array([[2,4,6],[1,3,5]])
# trans1=sp.fft(var1)
#
# print(trans1)

import numpy as np
from scipy.fft import fft

var1 = np.array([[2, 4, 6], [1, 3, 5]])
trans1 = fft(var1, axis=1)  # FFT along each row

print(trans1)
