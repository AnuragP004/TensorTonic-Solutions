import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    res = np.array([np.percentile(x,y,method = 'linear') for y in q])
    return res