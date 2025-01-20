import numpy as np

def CosineSmooth(y, window_size):
    """
    Smooth a function based on a cosine kernel of size equal to window_size.

    Parameters
    --------
    y : array_like
    1 dimensional input array

    window_size : int
    window size for smoothening

    Returns
    --------
    y : array_like
    smoothed array
    """
    # Add padding to the input array
    y = np.pad(y, (window_size, window_size), mode='reflect')

    x = np.arange(0,window_size,1)

    # Convert window size to frequency for consine function
    frequency = np.pi/window_size

    # Convolution between the input array and a cosine function with frequency adapted to window size    
    smooth = np.convolve(y, np.cos(frequency*(x - window_size//2))/window_size, mode='same')

    # Return smoothed array without padding
    return smooth[window_size:-window_size]
