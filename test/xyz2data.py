import numpy as np
num_atoms = 78
num_types = 3
C_type = 1
H_type = 2
N_type = 3

mass_C = 12.0107
mass_H = 1.0080
mass_N = 14.067

atom_section = []
count = 0
l = 40.0 
box_length = [l, l, l]
xlo = -box_length[0]/2
xhi = box_length[0]/2
ylo = -box_length[1]/2
yhi = box_length[1]/2
zlo = -box_length[2]/2
zhi = box_length[2]/2

header = '# converting xyz file to data file.'

file_in = open('pan.xyz', 'r')
file_out = open('pan.data', 'w')

file_out.write('%s\n\n' % header)
file_out.write('%d\t %s\n' % (num_atoms, 'atoms'))
file_out.write('%d\t %s\n\n' % (num_types, 'atom types'))
file_out.write('%f %f\t %s\n' % (xlo, xhi, 'xlo xhi'))
file_out.write('%f %f\t %s\n' % (ylo, yhi, 'ylo yhi'))
file_out.write('%f %f\t %s\n\n' % (zlo, zhi, 'zlo zhi'))
file_out.write('%s\n\n' % 'Masses')
file_out.write('%d\t %f\n' % (C_type, mass_C))
file_out.write('%d\t %f\n' % (H_type, mass_H))
file_out.write('%d\t %f\n\n' % (N_type, mass_N))
file_out.write('%s\n\n' % 'Atoms')

lines = file_in.readlines()[2:num_atoms+2]

for line in lines:
    count = count + 1
    row = line.split()
    if row[0] == 'C':
        atom_section.append([count, C_type, float(0), float(row[1]), float(row[2]), float(row[3])])

    elif row[0] == 'H':
        atom_section.append([count, H_type, float(0), float(row[1]), float(row[2]), float(row[3])])

    elif row[0] == 'N':
        atom_section.append([count, N_type, float(0), float(row[1]), float(row[2]), float(row[3])])

coord = np.array(atom_section)

xyz = np.array([min(coord[:,3]), max(coord[:,3]),
                min(coord[:,4]), max(coord[:,4]),
                min(coord[:,5]), max(coord[:,5])])

centroid = np.array([0.5*(xyz[1]-xyz[0]),
                     0.5*(xyz[3]-xyz[2]),
                     0.5*(xyz[5]-xyz[4])])

Coord = np.subtract(coord[:,3:6], np.array([0,0,0]))

for i in range(len(atom_section)-1):
    file_out.write('%d\t %d\t %f\t %f\t %f\n' % 
                   (atom_section[i][0], atom_section[i][1], Coord[i][0], Coord[i][1], Coord[i][2]))

file_out.write('%d\t %d\t %f\t %f\t %f' % 
                   (atom_section[-1][0], atom_section[-1][1], Coord[-1][0], Coord[-1][1], Coord[-1][2]))
file_in.close()
file_out.close()
