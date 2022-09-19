
import numpy as np 
from numpy.ctypeslib import ndpointer 
import ctypes
from ctypes import c_int 
import pathlib



if __name__ == "__main__":
    clibrary = ctypes.CDLL("C:\codigosAlgoritmia\helloWorld\clibrary.so")

    clibrary.cprint_array.restype = ctypes.c_void_p
    # Define arguments
    singlepp = ndpointer(dtype = np.int32, ndim = 1, flags = 'C') 
    clibrary.cprint_array.argtypes = [singlepp, ctypes.c_int]

    # Define ndarray
    x = np.arange(21, dtype = np.int32 )

    # Define the m parameter for the array len 
    m = ctypes.c_int(x.shape[0])

    clibrary.cprint_array(x,m)