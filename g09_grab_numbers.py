
def find_n_elect(file_name):
    log_file = open('%s.log' % file_name)
    for line in log_file:
        if 'alpha electrons' in line:
            alpha = int(line.split()[0])
            beta  = int(line.split()[3])
            n_ele = alpha + beta
            break
    return n_ele, alpha, beta

def find_homo(file_name):
    log_file = open('%s.log' % file_name)
    occ_orbitals = []
    for line in log_file:
        if 'Alpha  occ. eigenvalues' in line:
            i = 4
            while i < len(line.split()):
                occ_orbitals.append(float(line.split()[i]))
                i += 1
        elif 'Beta  occ. eigenvalues' in line:
            i = 4
            while i < len(line.split()):
                occ_orbitals.append(float(line.split()[i]))
                i += 1 
    return max(occ_orbitals)

def find_lumo(file_name):
    log_file = open('%s.log' % file_name)
    occ_orbitals = []
    for line in log_file:
        if 'Alpha virt. eigenvalues' in line:
            i = 4
            while i < len(line.split()):
                occ_orbitals.append(float(line.split()[i]))
                i += 1
        elif 'Beta virt. eigenvalues' in line:
            i = 4
            while i < len(line.split()):
                occ_orbitals.append(float(line.split()[i]))
                i += 1 
    return min(occ_orbitals)

def find_scf_energy(file_name):
    log_file = open('%s.log' % file_name)
    for line in log_file:
        if 'SCF Done:' in line:
            energy = float(line.split()[4])
    return energy

def grab_coords(log_file):
    log_file = open('%s.log' % log_file)
    coords = []
    for line in log_file:
        if 'Optimization completed.' in line:
            break

    for line in log_file:
        if 'Standard orientation:' in line:
            break

    line = log_file.next()
    line = log_file.next()
    line = log_file.next()
    line = log_file.next()
    for line in log_file:
        if '-----------' in line:
           break
        else:
            a, b, c, d, e, f = line.split()
            coords.append([b, float(d), float(e), float(f)])

    return coords




