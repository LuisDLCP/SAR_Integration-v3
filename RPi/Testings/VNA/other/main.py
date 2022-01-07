#!/home/soporte/anaconda3/bin/python3

import vna2 as v
import numpy as np
import h5py

m = v.vnaClient()
m.connect()
m.send_idn()
m.send_ifbw(ifbw=100)
m.send_number_points(points=20)
m.send_freq_start(freq_start=13)
m.send_freq_stop(freq_stop=15)
m.send_power(power=-5)
m.send_cfg()

# Save dataset as HDF5 file
data = m.send_sweep()
hf = h5py.File("data2.hdf5", 'w')
hf.create_dataset("dataset_1", data=data)
hf.close()

m.close()
