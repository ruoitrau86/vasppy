import numpy as np
import re

def reciprocal_lattice_from_outcar( filename ): # from https://github.com/MaterialsDiscovery/PyChemia
    """
    Finds and returns the reciprocal lattice vectors, if more than
    one set present, it just returns the last one.
    Args:
        filename (Str): The name of the outcar file to be read

    Returns:
        List(Float): The reciprocal lattice vectors.
    """
    outcar = open(filename, "r").read()
    # just keeping the last component
    recLat = re.findall(r"reciprocal\s*lattice\s*vectors\s*([-.\s\d]*)",
                        outcar)[-1]
    recLat = recLat.split()
    recLat = np.array(recLat, dtype=float)
    # up to now I have, both direct and rec. lattices (3+3=6 columns)
    recLat.shape = (3, 6)
    recLat = recLat[:, 3:]
    return recLat

def final_energy_from_outcar( filename='OUTCAR' ):
    """
    Finds and returns the energy from a VASP OUTCAR file, by searching for the last `energy(sigma->0)` entry.

    Args:
        filename (Str, optional): OUTCAR filename. Defaults to 'OUTCAR'.

    Returns:
        (Float): The last energy read from the OUTCAR file.
    """
    with open( filename ) as f:
        outcar = f.read()
    energy_re = re.compile( "energy\(sigma->0\) =\s+([-\d\.]+)" )
    energy = float( energy_re.findall( outcar )[-1] )
    return energy
       
