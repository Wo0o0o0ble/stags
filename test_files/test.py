import sys
sys.path.append('../')
import qe_data_grab as qe
import g09_grab_numbers as g09

print "     find_scf_energy('anti_tagfem_qe432.scf.out') gives %15.9f as the scf energy" % qe.find_scf_energy('anti_tagfem_qe432.scf.out')
print "  find_nonxdm_energy('anti_tagfem_qe432.scf.out') gives %15.9f as the scf energy with no xdm correction" % qe.find_nonxdm_energy('anti_tagfem_qe432.scf.out')[0]
print "  find_nonxdm_energy('anti_tagfem_qe432.scf.out') gives %15.9f as the xdm correction" % qe.find_nonxdm_energy('anti_tagfem_qe432.scf.out')[1]
print "            find_mag('anti_tagfem_qe432.scf.out') gives %15.9f as the total magnetisation" % qe.find_mag('anti_tagfem_qe432.scf.out')[0]
print "            find_mag('anti_tagfem_qe432.scf.out') gives %15.9f as the absolute magnetisation" % qe.find_mag('anti_tagfem_qe432.scf.out')[1]
print "find_unitcell_volume('anti_tagfem_qe432.scf.out') gives %15.9f as the unit cell volume" % qe.find_unitcell_volume('anti_tagfem_qe432.scf.out')
print "                   find_nnm('anti_tagfem.yt.out') gives %15.9f as the number of nnm" % qe.find_nnm('anti_tagfem.yt.out')[0]
print "                   find_nnm('anti_tagfem.yt.out') gives %15.9f as the total charge localised in nnm" % qe.find_nnm('anti_tagfem.yt.out')[1]
print "                   find_nnm('anti_tagfem.yt.out') gives %15.9f as the total volume occupied by nnm" % qe.find_nnm('anti_tagfem.yt.out')[2]
print "      find_pro_void_volume('anti_tagfem.nci.out') gives %15.9f as the promolecular void volume" % qe.find_pro_void_volume('anti_tagfem.nci.out')
print "           find_homo('anti_tagfem_qe432.scf.out') gives %15.9f as the homo energy" % qe.find_homo('anti_tagfem_qe432.scf.out', 0)
print "           find_lumo('anti_tagfem_qe432.scf.out') gives %15.9f as the lumo energy" % qe.find_lumo('anti_tagfem_qe432.scf.out', 0)
print "          find_fermi('anti_tagfem_qe432.scf.out') gives %15.9f as the fermi energy" % qe.find_lumo('anti_tagfem_qe432.scf.out')
print "                 grab_coords('ca2n-exfo.scf.out') gives the coordinates of the last relaxation step "
coords, cell = qe.grab_coords('ca2n-exfo.scf.out')
print "       ATOMIC POSITIONS         "
for i in coords:
    print "%10.3s %10.6f %10.6f %10.6f" % (i[0], i[1], i[2], i[3])
print "       CELL PARAPETERMS         "
for i in cell:
    print "%10.6f %10.6f %10.6f" % (i[0], i[1], i[2])
print "                   find_n_elect('li-9c3.log') gives %15.9f electrons" % g09.find_n_elect('li-9c3.log')[0]
print "                   find_n_elect('li-9c3.log') gives %15.9f alpha electrons" % g09.find_n_elect('li-9c3.log')[1]
print "                   find_n_elect('li-9c3.log') gives %15.9f beta electrons" % g09.find_n_elect('li-9c3.log')[2]
print "                      find_homo('li-9c3.log') gives %15.9f as the homo energy" % g09.find_homo('li-9c3.log')
print "                      find_lumo('li-9c3.log') gives %15.9f as the lumo energy" % g09.find_lumo('li-9c3.log')
print "                find_scf_energy('li-9c3.log') gives %15.9f as the scf energy" % g09.find_scf_energy('li-9c3.log')
print "               find_ccsdt_energy('bh22f.log') gives %15.9f as the ccsd(t) energy" % g09.find_ccsdt_energy('bh22f.log')
print "                find_ccsd_energy('bh22f.log') gives %15.9f as the ccsd energy" % g09.find_ccsd_energy('bh22f.log')
print "               find_xdm_energy('co2_co2.log') gives %15.9f as the total energy" % g09.find_xdm_energy('co2_co2.log')[0]
print "               find_xdm_energy('co2_co2.log') gives %15.9f as the diespersion energy" % g09.find_xdm_energy('co2_co2.log')[1]
print "                     find_polar('h4-mp4.log') gives %15.9f as the a_zz dipole moment" % float(g09.find_polar('h4-mp4.log')[5])
print "                find_hyperpolar('h4-mp4.log') gives %15.9f as the b_zzz hyperpolarisability" % float(g09.find_hyperpolar('h4-mp4.log')[9])
print "                       find_B05('h4-000.out') gives %15.9f as the B05 energy" % g09.find_B05('h4-000.out')[0]
print "                       find_B05('h4-000.out') gives %15.9f as the B13-0 energy" % g09.find_B05('h4-000.out')[1]
print "                       find_dipole('hcn.log') gives %15.9f as the absolute dipole moment" % g09.find_dipole('hcn.log')
print "                    grab_coords('li-9c3.log') gives the coordinates of the last optimization step"
coords = g09.grab_coords('li-9c3.log')
for i in coords:
    print "%10.3s %10.6f %10.6f %10.6f" % (i[0], i[1], i[2], i[3])
print "                         find_mull('hcn.log') gives the mulliken charges of each atom"
mull = g09.find_mull('hcn.log')
for i in mull:
    print "%10.3s %10.4f" % (i[0], i[1])
print "                        find_hirsh('hcn.log') gives the hirshfeld charges of each atom"
hirsh = g09.find_hirsh('h2o.log')
for i in hirsh:
    print "%10.3s %10.4f" % (i[0], i[1])



