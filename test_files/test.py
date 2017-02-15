import sys
sys.path.append('../')
import qe_data_grab as qe
import g09_grab_numbers as g09

print "     find_scf_energy('anti_tagfem_qe432') gives %15.9f as the scf energy" % qe.find_scf_energy('anti_tagfem_qe432')
print "  find_nonxdm_energy('anti_tagfem_qe432') gives %15.9f as the scf energy with no xdm correction" % qe.find_nonxdm_energy('anti_tagfem_qe432')[0]
print "  find_nonxdm_energy('anti_tagfem_qe432') gives %15.9f as the xdm correction" % qe.find_nonxdm_energy('anti_tagfem_qe432')[1]
print "            find_mag('anti_tagfem_qe432') gives %15.9f as the total magnetisation" % qe.find_mag('anti_tagfem_qe432')[0]
print "            find_mag('anti_tagfem_qe432') gives %15.9f as the absolute magnetisation" % qe.find_mag('anti_tagfem_qe432')[1]
print "find_unitcell_volume('anti_tagfem_qe432') gives %15.9f as the unit cell volume" % qe.find_unitcell_volume('anti_tagfem_qe432')
print "                  find_nnm('anti_tagfem') gives %15.9f as the number of nnm" % qe.find_nnm('anti_tagfem')[0]
print "                  find_nnm('anti_tagfem') gives %15.9f as the total charge localised in nnm" % qe.find_nnm('anti_tagfem')[1]
print "                  find_nnm('anti_tagfem') gives %15.9f as the total volume occupied by nnm" % qe.find_nnm('anti_tagfem')[2]
print "      find_pro_void_volume('anti_tagfem') gives %15.9f as the promolecular void volume" % qe.find_pro_void_volume('anti_tagfem')
print "           find_homo('anti_tagfem_qe432') gives %15.9f as the homo energy" % qe.find_homo('anti_tagfem_qe432', 0)
print "           find_lumo('anti_tagfem_qe432') gives %15.9f as the lumo energy" % qe.find_lumo('anti_tagfem_qe432', 0)
print "          find_fermi('anti_tagfem_qe432') gives %15.9f as the fermi energy" % qe.find_lumo('anti_tagfem_qe432')
print "                 grab_coords('ca2n-exfo') gives the coordinates of the last relaxation step "
coords, cell = qe.grab_coords('ca2n-exfo')
print "       ATOMIC POSITIONS         "
for i in coords:
    print "%10.3s %10.6f %10.6f %10.6f" % (i[0], i[1], i[2], i[3])
print "       CELL PARAPETERMS         "
for i in cell:
    print "%10.6f %10.6f %10.6f" % (i[0], i[1], i[2])
print "                   find_n_elect('li-9c3') gives %15.9f electrons" % g09.find_n_elect('li-9c3')[0]
print "                   find_n_elect('li-9c3') gives %15.9f alpha electrons" % g09.find_n_elect('li-9c3')[1]
print "                   find_n_elect('li-9c3') gives %15.9f beta electrons" % g09.find_n_elect('li-9c3')[2]
print "                      find_homo('li-9c3') gives %15.9f as the homo energy" % g09.find_homo('li-9c3')
print "                      find_lumo('li-9c3') gives %15.9f as the lumo energy" % g09.find_lumo('li-9c3')
print "                find_scf_energy('li-9c3') gives %15.9f as the scf energy" % g09.find_scf_energy('li-9c3')
print "               find_xdm_energy('co2_co2') gives %15.9f as the total energy" % g09.find_xdm_energy('co2_co2')[0]
print "               find_xdm_energy('co2_co2') gives %15.9f as the diespersion energy" % g09.find_xdm_energy('co2_co2')[1]
print "                    grab_coords('li-9c3') gives the coordinates of the last optimization step"
coords = g09.grab_coords('li-9c3')
for i in coords:
    print "%10.3s %10.6f %10.6f %10.6f" % (i[0], i[1], i[2], i[3])

