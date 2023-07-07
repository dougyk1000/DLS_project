def read_phases(l):

    phases2 = []
    with open(f'D:\\my_pyhton_projects\\nn_sarov\\best_version\\fi_finished\\fi_finished{l}.txt') as f:
        phases = f.readline().replace('[', '').replace(']', '').replace('\n', '').split()

    for i in range(4):
        phases2.append(float(phases[i]))
    return phases2


def read_phases2(l):
    phases2 = []
    with open(f'D:\\my_pyhton_projects\\nn_sarov\\best_version\\fi_initial\\fi_initial{l}.txt') as f:
        phases = f.readline().replace('[', '').replace(']', '').replace('\n', '').replace(',', '').split()

    for i in range(4):
        phases2.append(float(phases[i]))
    return phases2


for l in range(1, 65537):
    fi = [i - k for i, k in zip(read_phases(l), read_phases2(l))]
    if l % 655 == 0:
        print(l // 655, '%')
    f1 = open(f'D:\\my_pyhton_projects\\nn_sarov\\best_version\\Y_train\\delta{l}.txt', 'w')
    f1.write(str(fi))
    f1.close()
