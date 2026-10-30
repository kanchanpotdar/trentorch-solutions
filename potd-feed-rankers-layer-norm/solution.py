import numpy as np

def feed_ranker_layer_norm(x: np.ndarray, eps: float) -> np.ndarray:
    """
    x: length-d feature vector.
    eps: small positive constant.

    mu = mean(x)
    v = population variance of x (divide by d, not d - 1)
    xhat_i = (x_i - mu) / sqrt(v + eps)

    No learnable scale or bias. Return xhat.
    """
    # Calculate the mean of the features
    mu = np.mean(x)
    
    # Calculate population variance. np.var uses ddof=0 by default (divides by d)
    v = np.var(x)
    
    # Normalize with epsilon for numerical stability
    xhat = (x - mu) / np.sqrt(v + eps)
    
    return xhat
