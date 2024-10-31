from scipy.io import loadmat

def load_mat_data(file_path):
    data = loadmat(file_path)
    
    x = data['x'].flatten()
    d = data['d'].flatten()
    miu = data['miu'].item()
    ord = data['ord'].item()
    p = data['p'].item()
    dlt = data['dlt'].item()
    a = data['a'].item()
    h1 = data['h1'].flatten()
    N = len(x)
    
    return x, d, miu, ord, p, dlt, a, h1, N