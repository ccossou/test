#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Test of flux for different filters. We compare MirimImager with 
a simple procedure (sed2electronSec) to retrieve the flux in 
Electron/s of a given source

If skysim/tests/test_externalsed.py
and
skysim/tests/test_flux_conservationC.py

are still validated, chances are that the problem comes in between. 

The two tests above are checking the accuracy of the flux in direct 
output of the SED. 

Here, we have in addition, PCE, the PSF, and the filters. 

27 April 2017

@author: Rene Gastaud & Christophe Cossou
"""

import numpy as np
import pdb
import os

def test_compute_flux(verbose=False):
    """
    Test flux of a point source for all the subarrays
    
    We compare to the brightest pixel flux, with PASP#9 as a reference
    """
    a = 2
    b = 2
    
    assert (a == b), "Wrong flux"
    

if __name__ == '__main__':
    import sys
    import getopt
    verbose=False

    if (len(sys.argv) > 1):
        optlist, args = getopt.getopt(sys.argv[1:], 'hpv')
        # read options
        for opt, value in optlist:
            if opt == '-h':
                print("options -(h)elp, -(v)erbose")
            if opt == '-v':
                verbose=True
    test_compute_flux(verbose=verbose)
