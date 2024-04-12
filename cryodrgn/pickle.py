import numpy as np
import pickle

poses = np.load('/scratch/network/jj4485/MFN/data/images/N10000_snr1.0/poses.npy')
pickle.dump(poses, open('/path/to/output_pose.pkl','wb'))

