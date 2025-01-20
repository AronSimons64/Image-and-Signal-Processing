import numpy as np
from scipy.optimize import curve_fit
from functools import partial

def fitfun(x, a, b, x0,x1 = 0, c = 0, fittype='s'):
      """
      List of to-be-fitted function depending on fittype parameter.
      Use case: fit = partial(fit,fittype="<str>"). No need to specify the fit parameters a,b,c,x0.
  
      Parameters
      ---------
      x : array_like
      x_array of fit function f(x)
  
      fittype : str
      string to filter the type of fit required
  
      Returns
      ----------
      f : fit variable
      contains the fitted function corresponding to the fit type provided
      """
      if fittype == 'p2':#Poly 2nd order
          f = a*(x-x0)**2 + b*(x-x0) + c
  
      return f

def poly_detrend(I, c = 0, debug = False):
    """
    Function that uses polynomial fitting to detrend a 1D signal.

    Parameters
    ----------
    I : array_like
        1D input array
    
    c : int
        cut-off value for signal

    debug : bool, optional
        Set True to activate debugger for this function.
    
    Returns
    ----------
    I' : array_like
        detrended array

    p : array_like
        List of the four fitting parameters a,b,c,x0 of fit(x) = a*(x-x0)**2 + b*(x-x0) + c.
    """
    
    fit = partial(fitfun,fittype='p2')
    
    Ip = I[c:]
    Ip = Ip/np.max(Ip)
    I = I/np.max(I)
    
    x = np.arange(len(Ip))

    # Initial parameters. Trend should be constant, so a = b = 0 and there should not be an offset x0 = 0. A constant trend must occur at the mean of the signal.
    p0 = [0,0,np.mean(Ip),0]

    param,cov = curve_fit(fit,x,Ip,p0)
    
    
    if debug == True:
        plt.title('signal detrending')
        plt.plot(Ip,label=f'original signal with cutoff = {c:.1f}')
        plt.plot(fit(x,*param),color='red',label='polynomial fit')
        plt.plot(Ip/fit(x,*param),color='green',label='detrended signal')
        plt.legend()
        plt.show()

    x = np.arange(len(I))
    I_detrended = I/fit(x,*param)

    # Renormalize 
    I_detrended = normalize(I_detrended)

    if debug == True:
        plt.title('signal detrending')
        plt.plot(I,label='original signal')
        plt.plot(I_detrended,color='green',label='detrended signal')
        plt.legend()
        plt.show()
    return I_detrended, param
