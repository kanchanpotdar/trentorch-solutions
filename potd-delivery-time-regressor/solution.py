import numpy as np

def delivery_time_regressor(x: np.ndarray, y: np.ndarray, queries: np.ndarray) -> tuple[float, np.ndarray, np.ndarray]:
    """
    x: n x d training feature matrix.
    y: length-n training targets.
    queries: m x d feature matrix to predict for.
    """
    # 1. Augment training matrix X with a column of ones for the intercept
    n = x.shape[0]
    ones_column = np.ones((n, 1))
    X_aug = np.hstack((ones_column, x))
    
    # 2. Fit minimum-norm least-squares solution w = X+ y
    # Using np.linalg.pinv uses SVD under the hood for numerical stability
    w = np.linalg.pinv(X_aug) @ y
    
    # 3. Extract intercept and coefficients
    intercept = float(w[0])
    coefficients = w[1:]
    
    # 4. Predict on the query data: yhat = w_0 + q @ w_1:d
    predictions = queries @ coefficients + intercept
    
    return intercept, coefficients, predictions
