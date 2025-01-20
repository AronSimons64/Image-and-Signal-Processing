import numpy as np

def transformation(y,n):
    """
        Transformation function to increase contrast in a 1D signal. 

        Parameters
        ----------
        y : array_like
        1D array of signal

        n : float
        mean noise magnitude of signal

        Returns
        ---------

        g : array_like
        function containing transformation values
    """
    # initialize g
    g = np.zeros(len(y))

    # Define threshold using variance of noise in derivative --> sqrt(2)*noise.
    dy = abs(np.diff(y))[1:]
    dy = normalize(dy)

    strictness = 2 # Set to 1, 2 or 3 to define how strict the threshold must be.
    threshold = (np.mean(dy) + strictness*np.sqrt(2)*n)

    # Find changes in signal (steps, could be plateau or peak)
    step_indices = [i + 2 for i in range(len(dy)) if abs(dy[i]) > threshold]

    # Add the first and last coordinate
    steps = np.append(0,step_indices)
    steps = np.append(steps,len(y))

    # Convert to list of integers
    steps = [int(i) for i in steps]

    # Find heights of each step
    heights =[np.mean(y[steps[i]:steps[i+1]]) for i in range(len(steps) - 1)]

    # Define transformation function
    for i in range(len(steps) - 1):
        g[steps[i]:steps[i+1]] = heights[i]/len(heights)*y[steps[i]:steps[i+1]]

    return g
