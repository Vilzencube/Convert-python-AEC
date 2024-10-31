import numpy as np
from Loader import load_mat_data
from Plot import *
from modify import modify

file_path = 'D:\\De_tai_sinh_vien\\code_chuan\\sound\\ex_eusipco_2010.mat'
x, d, miu, ord, p, dlt, a, h1, N = load_mat_data(file_path)
my_list = []
t = np.linspace(0, N / 8000, N)

for select in range(1, 6):
    m, w = modify(x, d, miu, ord, p, dlt, a, h1, select)
    my_list.append(m)
    plot_one_misalignment(t, m, select)

plot_misalignment(t, my_list)
