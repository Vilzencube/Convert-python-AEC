import numpy as np
import matplotlib.pyplot as plt


link = 'D:\\De_tai_sinh_vien\\code_chuan\\figure\\'

def plot_one_misalignment(t, m, select):
    fig, ax = plt.subplots()
    #ax.plot(t, m, color='blue', linewidth=0.5)  # Change the color to blue and increase the linewidth
    ax.set_xlabel('Time (seconds)', fontsize=10, fontweight='bold')
    if select == 1:
        ax.plot(t, m, color='black', linewidth=0.2)
        ax.set_ylabel('AMIPAPA', fontsize=10, fontweight='bold')
    elif select == 2:
        ax.plot(t, m, color='blue', linewidth=0.2)
        ax.set_ylabel('IPAPA', fontsize=10, fontweight='bold')
    elif select == 3:
        ax.plot(t, m, color='red', linewidth=0.2)
        ax.set_ylabel('NLMS', fontsize=10, fontweight='bold')
    elif select == 4:
        ax.plot(t, m, color='purple', linewidth=0.2)
        ax.set_ylabel('APA', fontsize=10, fontweight='bold')
    elif select == 5:
        ax.plot(t, m, color='green', linewidth=0.2 , linestyle='--')
        ax.set_ylabel('IPNLMS', fontsize=10, fontweight='bold')

    # Set the origin (0,0) to align with the bottom-left corner
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', -25))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Ensure the axes start from 0 on x-axis and include -8 on y-axis
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=-25)

    # Increase the tick frequency on the x-axis
    ax.set_xticks(np.arange(0, max(t)+0.1, step=0.1))  # Adjust the step value to 0.1

    # Save the figure
    if select == 1:
        plt.savefig('D:\\De_tai_sinh_vien\\code_chuan\\figure\\AMIPAPA.png')
    elif select == 2:
        plt.savefig('D:\\De_tai_sinh_vien\\code_chuan\\figure\\IPAPA.png')
    elif select == 3:
        plt.savefig('D:\\De_tai_sinh_vien\\code_chuan\\figure\\NLMS.png')
    elif select == 4:
        plt.savefig('D:\\De_tai_sinh_vien\\code_chuan\\figure\\APA.png')
    elif select == 5:
        plt.savefig('D:\\De_tai_sinh_vien\\code_chuan\\figure\\IPNLMS.png')
    #plt.show()

def plot_misalignment(t, m_list):
    fig, ax = plt.subplots()
    colors = ['black'  , 'blue',  'red',  'purple',  'green']
    labels = ['AMIPAPA', 'IPAPA', 'NLMS', 'APA'   ,  'IPNLMS']

    for i, m in enumerate(m_list):
        ax.plot(t, m, color=colors[i], linewidth=0.5, label=labels[i])

    ax.set_xlabel('Time (seconds)', fontsize=10, fontweight='bold')
    ax.set_ylabel('Misalignment', fontsize=10, fontweight='bold')

    # Set the origin (0,0) to align with the bottom-left corner
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', -25))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Ensure the axes start from 0 on x-axis and include -8 on y-axis
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=-25)

    # Increase the tick frequency on the x-axis
    ax.set_xticks(np.arange(0, max(t)+0.1, step=0.1))  # Adjust the step value to 0.1

    # Add legend
    ax.legend()

    # Save the figure
    plt.savefig('D:\\De_tai_sinh_vien\\code_chuan\\figure\\combined_plot.png')
    plt.show()