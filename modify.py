import numpy as np

def modify(x, d, miu , ord , p , dlt ,a , h1 , select):

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

    # AMIPAPA
    if select == 1:
        for n in range(N):
            x1 = np.concatenate(([x[n]], x1[:ord-1]))
            X = np.column_stack((x1, X[:, :p-1]))
            D = np.concatenate(([d[n]], D[:p-1]))
            Y = X.T @ w
            E = D - Y
            kd = (1 - a) / (2 * ord) + (1 + a) * np.abs(w) / (10**-8 + 2 * np.sum(np.abs(w)))

            P = np.column_stack((kd * x1, P[:, :p-1]))
            t = X.T @ P[:, 0]
            S[0, :] = t
            S[:, 0] = t

            if n < 100:
                S[0, 0] += 100 * dlt
            else:
                S[0, 0] += dlt

            S[1:p, 1:p] = S0[:p-1, :p-1]
            S0 = S.copy()
            w = w + miu * P @ np.linalg.inv(S) @ E
            m[n] = 20 * np.log10(np.linalg.norm(w - h1) / np.linalg.norm(h1))

    #IPAPA
    elif select == 2:
        for n in range(N):
            x1 = np.concatenate(([x[n]], x1[:ord-1]))
            X = np.column_stack((x1, X[:, :p-1]))
            D = np.concatenate(([d[n]], D[:p-1]))
            Y = X.T @ w
            E = D - Y

            kd = (1-a) / (2 * ord) + (1 + a) * np.abs(w) / (10**-8 + 2 * np.sum(np.abs(w)))
            P = np.column_stack((kd * x1, P[:, :p-1]))

            S = dlt * np.eye(p) + X.T @ P
            E2 = E.T @ np.linalg.inv(S)
            w = w + miu * P @ E2.T
            m[n] = 20 * np.log10(np.linalg.norm(w - h1) / np.linalg.norm(h1))

    #NLMS 
    elif select == 3 :
        for n in range(N):
            x1 = np.concatenate(([x[n]], x1[:ord-1]))
            ep = d[n] - np.dot(x1, w)
            w = w + miu / (np.linalg.norm(x1)**2 + 1e-8) * x1 * ep
            m[n] = 20 * np.log10(np.linalg.norm(w - h1) / np.linalg.norm(h1))

    #APA
    elif select == 4:
        for n in range(N):
            x1 = np.concatenate(([x[n]], x1[:ord-1]))
            X = np.column_stack((x1, X[:, :p-1]))
            D = np.concatenate(([d[n]], D[:p-1]))
            E = D - X.T @ w

            w = w + miu * X @ np.linalg.inv(dlt * np.eye(p) + X.T @ X) @ E
            m[n] = 20 * np.log10(np.linalg.norm(w - h1) / np.linalg.norm(h1))
    #IPNLMS
    elif select ==  5:
        for n in range(N):
            x1 = np.concatenate(([x[n]], x1[:ord-1]))
            ep = d[n] - np.dot(x1, w)

            kd = (1 - a) / (2 * ord) + (1 + a) * np.abs(w) / (1e-8 + 2 * np.sum(np.abs(w)))
            Kd = np.diag(kd)
            w = w + (miu / (np.dot(x1.T, np.dot(Kd, x1)) + 1e-8 * (1 - a) / (2 * ord))) * np.dot(Kd, x1) * ep

            m[n] = 20 * np.log10(np.linalg.norm(w - h1) / np.linalg.norm(h1))


    return m , w