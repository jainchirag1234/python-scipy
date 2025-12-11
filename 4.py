import scipy as sp
from scipy import integrate

var1=lambda x:x**3
function1=integrate.quad(var1,0,6)
print(function1)
