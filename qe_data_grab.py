import re

# Find last SCF energy in a qe output
def find_scf_energy(file_name):
    energy = 0.
    test = 0
    scf_out = open('%s.scf.out' % file_name, 'r')
    for line in scf_out:
        if '!' in line:
            energy = float(line.split()[4])
    #Discard if Job did not complete correctly
        elif 'JOB DONE' in line:
            test = 1
    if test == 0:
        energy = 0.0
    return energy

# Find the last xdm correction and uncorrected SCF energy in a qe output
def find_nonxdm_energy(file_name):
    scf_out = open('%s.scf.out' % file_name, 'r')
    ene = 0.
    test = 0
    xdm = 0.
    for line in scf_out:
        if 'Dispersion XDM Correction' in line:
            xdm = float(line.split()[4])
        elif '!' in line:
            ene = float(line.split()[4])
        elif 'JOB DONE' in line:
            test = 1
    if test == 0:
        ene = 0.0
	xdm = 0.
    bare = ene - xdm
    return bare, xdm

# Find the magnetization of a qe output
def find_mag(file_name):
    scf_out = open('%s.scf.out' % file_name, 'r')
    tot_mag, abs_mag = 0, 0
    for line in scf_out:
        if 'total magnetization' in line:
            tot_mag = float(line.split()[3])
        if 'absolute magnetization' in line:
            abs_mag = float(line.split()[3])
    return tot_mag, abs_mag

# find the unitcell volume qe output
def find_unitcell_volume(file_name):
    scf_out = open('%s.scf.out' % file_name, 'r')
    for line in scf_out:
        if 'unit-cell volume' in line:
            unitcell_volume = float(line.split()[3])
            break
    return unitcell_volume

# Find the total charge localised in nnm calculated from the critic2 program
def find_nnm(file_name):
    no_nnm = 0
    bader_charge = 0
    bader_volume = 0
    nnm_m = re.compile(' n..  ')
    yt_out = open('%s.yt.out' % file_name, 'r')
    for line in yt_out:
        if '* List of basins and local properties' in line:
            break
        elif '* Integrated atomic properties' in line:
            break
    for line in yt_out:
        if 'nnm' in  line:
            line_nnm = re.sub('nnm', 'nnm  ', line)
            no_nnm += 1
            bader_charge += float(line_nnm.split()[6])
            bader_volume += float(line_nnm.split()[5])
        if re.search(nnm_m, line) != None:
            if 'ncp' in line:
                continue
            no_nnm += 1
            bader_charge += float(line.split()[6])
            bader_volume += float(line.split()[5])
        if ' ?? ' in line:
            no_nnm += 1
            bader_charge += float(line.split()[7])
            bader_volume += float(line.split()[6])
    return no_nnm, bader_charge, bader_volume

# find the void volume calculated from the nci program
def find_pro_void_volume(file_name):
    nci_out = open('%s.nci.out' % file_name, 'r')
    for line in nci_out:
        if 'Void volume' in line:
            pro_void_volume = float(line.split()[-1])
            break
    return pro_void_volume

# Find the homo or appropriate (homo - n_loc) from a qe output 
# Needs more testing
def find_homo(file_name, n_loc = 0):
    infile = open('%s.scf.out' % file_name,'r')
    s_up = []
    for line in infile:
        if 'number of electrons' in line:
            n_ele = float(line.split()[4])
            break
    for line in infile:
        if 'SPIN UP' in line:
            break
    i = 0
    for line in infile:
        if i < 4:
            i += 1
            continue
        elif len(line) < 3:
            break
        else:
            hold = line.split()
            j = 0
            while j < len(hold):
                s_up.append(float(hold[j]))
                j += 1
    return s_up[int(n_ele)/2 + n_loc/2 - 1]

# Find the lumo or appropriate (lumo + n_loc) from a qe output 
# Needs more testing
def find_lumo(file_name, n_loc = 0):
    infile = open('%s.scf.out' % file_name,'r')
    s_dn = []
    for line in infile:
        if 'number of electrons' in line:
            n_ele = float(line.split()[4])
            break
    for line in infile:
        if 'SPIN DOWN' in line:
            break
    i = 0
    for line in infile:
        if i < 4:
            i += 1
            continue
        elif len(line) < 3:
            break
        else:
            hold = line.split()
            j = 0
            while j < len(hold):
                s_dn.append(float(hold[j]))
                j += 1
    return s_dn[int(n_ele)/2 - (n_loc/2 - 1) - 1]

# Find the fermi energy from a qe output
def find_fermi(file_name):
    infile = open('%s.scf.out' % file_name,'r')
    for line in infile:
        if 'the Fermi energy is' in line:
            fermi = line.split()[4]
    return fermi

# Find the calculated stress from a qe output
def find_stress(file_name):
    infile = open('%s.scf.out' % file_name, 'r')
    for line in infile:
	if 'total   stress' in line:
	    stress = float(line.split()[5])
    return stress

# Find final geometry in relaxation calculation
def grab_coords(file_name):
    cell = []
    coor = []
    infile = open('%s.scf.out' % file_name, 'r')
    for line in infile:
        if 'Begin final coordinates' in line:
            break
    for line in infile:
        if 'CELL_PARAMETERS' in line:
            break
    for line in infile:
        if 'End final coordinates' in line:
            break
        elif len(line.split()) == 3:
            a,b,c=line.split()
            cell.append([float(a), float(b), float(c)])
        elif len(line.split()) >= 4:
            coor.append([line.split()[0], float(line.split()[1]), float(line.split()[2]), float(line.split()[3])])

    return coor, cell


