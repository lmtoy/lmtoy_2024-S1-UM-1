#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-UM-1"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["NGC4388+vicinity"] = [ 
			   112458, 112459, 112461, 112462, 112466,
                           112467, 112469, 112470,
			   112708, 112709, 112713, 112714, 112718, 112719, 112723, 
                           # 112724, 
	                   112826, 112827, 112985, 112986, 112988, 112989, 
                           112995, 112996,
                           113129, 113130, 113132, 113133,
                           # inherit from 2023-S1-UM-8
			   109948, 109949, 109953, 109954, 109960, 109961, 110036, 110037,
			 ]

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["NGC4388+vicinity"] = "dv=250 dw=300 b_order=1"
#                         = "dv=350 dw=400 b_order=1 otf_cal=1"   # from UM-8


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["NGC4388+vicinity"] = ""

# no pars3, only bank=0 was observed

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
