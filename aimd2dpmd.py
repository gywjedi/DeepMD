import dpdata

# Parse QE MD output
system = dpdata.LabeledSystem("md.out", fmt="qe/pw/scf")

# Save to DeepMD format
system.to_deepmd_npy("deepmd_data")

