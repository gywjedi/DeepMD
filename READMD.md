#deePMD force field development
=================================================================
1. running QE ab-initio calculations to obtain the trajectories
2. convert the aimd trajectories to npy. dataset using dp data 
3. prepare a json file, training deep learning force field based on the dataset using dp train
4. freeze the machine learning force field using dp freeze -o frozen_model.pb
4. running lammps simulations use frozen_mode.pb
