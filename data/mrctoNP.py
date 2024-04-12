# Assume the classes MRCHeader and MRCFile are already defined as per your code.
from cryodrgn import mrc
from mrc import MRCHeader, MRCFile
import numpy as np
def convert_npy_to_mrc(npy_filename, mrc_filename, apix):
    # Load the numpy array from the .npy file
    npy_data = np.load(npy_filename)

    # Use the make_default_header class method to create a default MRC header
    # You need to know the pixel size (apix), which is the physical size of one voxel
    # For example, apix might be 1.0 angstrom/voxel
    header = MRCHeader.make_default_header(
        nz=npy_data.shape[0],
        ny=npy_data.shape[1],
        nx=npy_data.shape[2],
        data=npy_data,
        is_vol=True,  # Assuming this is volume data
        Apix=apix,  # Pixel size
    )

    # Write the MRC file using the MRCFile class
    MRCFile.write(mrc_filename, npy_data, header)

# Example usage of the function
npy_file_path = 'path/to/your/data.npy'  # Replace with your actual .npy file path
mrc_file_path = 'path/to/your/output.mrc'  # Replace with your desired output .mrc file path
angstrom_per_voxel = 1.0  # Replace with the actual pixel size

# Call the conversion function
convert_npy_to_mrc(npy_file_path, mrc_file_path, angstrom_per_voxel)
