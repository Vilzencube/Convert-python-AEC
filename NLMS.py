import numpy as np

def nlms_all_AEC(x, d, miu, ord, p, dlt, a, h1):
    N = len(x)  # length of data in
    w = np.zeros(ord)  # adaptive filter weights
    x1 = np.zeros(ord)
    D = np.zeros(p)
    X = np.zeros((ord, p))
    P = np.zeros((ord, p))
    m = np.zeros((N,1))
    e = np.zeros((N,1))
    S0 = dlt * np.eye(p)  # matrix two side p p  
    S = np.zeros((p, p))  # vector with dimension p p    

    for n in range(N):
        x1 = np.concatenate(([x[n]], x1[:ord-1]))
        ep = d[n] - np.dot(x1, w)
        w = w + miu / (np.linalg.norm(x1)**2 + 1e-8) * x1 * ep
        m[n] = 20 * np.log10(np.linalg.norm(w - h1) / np.linalg.norm(h1))
    return m, w