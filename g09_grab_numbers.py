import re

def find_n_elect(file_name):
    log_file = open('%s' % file_name)
    for line in log_file:
        if 'alpha electrons' in line:
            alpha = int(line.split()[0])
            beta  = int(line.split()[3])
            n_ele = alpha + beta
            break
    return n_ele, alpha, beta

def find_homo(file_name):
    log_file = open('%s' % file_name)
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
    log_file = open('%s' % file_name)
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
    energy = 0.
    log_file = open('%s' % file_name)
    for line in log_file:
        if 'SCF Done:' in line:
            energy = float(line.split()[4])
    return energy

def find_ccsdt_energy(file_name):
    energy = 0.
    log_file = open('%s' % file_name)
    for line in log_file:
        if 'CCSD(T)= ' in line:
            energy = float(line.split()[1].replace('D', 'E'))
            break
    return energy

def find_xdm_energy(file_name):
    log_file = open('%s' % file_name)
    for line in log_file:
        if 'total energy (SCF+XDM)' in line:
            tot_ene = float(line.split()[3])
        if 'dispersion energy' in line:
            disp_ene = float(line.split()[2])
    return tot_ene, disp_ene


def grab_coords(log_file):
    log_file = open('%s' % log_file)
    coords = []
    for line in log_file:
        if 'Optimization completed' in line:
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

# Returns polarisabilities read from a gaussian file as a list in the form
# [a_xx, a_xy, a_yy, a_xz, a_yz, a_zz]
def find_polar(log_file):
    log_file = open('%s' % log_file)
    collect = ''
    for line in log_file:
        if 'Version=' in line:
            break
        if 'State=' in line:
            break
    for line in log_file:
        collect += line
    collect = re.sub('\\n ', '', collect)
    polar = [0., 0., 0., 0., 0., 0.]
    for i in collect.split('\\'):
        if 'Polar' in i:
            polar = i.split('=')[1]
            polar = polar.split(',')
            break
    return polar

# Returns hyperpolarisabilities read from a gaussian file as a list in the form
# [b_xxx, b_xxy, b_xyy, b_yyy, b_xxz, b_xyz, b_yyz, b_xzz, b_yzz, b_zzz]
def find_hyperpolar(log_file):
    log_file = open('%s' % log_file)
    collect = ''
    for line in log_file:
        if 'Version=' in line:
            break
        if 'State=' in line:
            break
    for line in log_file:
        collect += line
    collect = re.sub('\\n ', '', collect)
    hpolar = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
    for i in collect.split('\\'):
        if 'HyperPolar' in i:
            hpolar = i.split('=')[1]
            hpolar = hpolar.split(',')
            break
    return hpolar

# Returns B05 and B13 energy read from the output file of Axels postG code (Apr 2017)
def find_B05(file_name):
    b05_out = open('%s' % file_name, 'r')
    B05 = 0.0
    B13 = 0.0
    for line in b05_out:
        if 'B05 energy' in line:
            B05 = float(line.split()[3])
        if 'B13-0 energy' in line:
            B13 = float(line.split()[3])
    return [B05, B13]








