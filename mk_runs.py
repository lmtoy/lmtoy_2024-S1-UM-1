#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-UM-1"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['foo'] = [ ]
on["NGC4388+vicinity"] = [ 112458, 112459, 112461, 112462, 112466,
                           112467, 112469, 112470,]

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["NGC4388+vicinity"] = ""

#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["NGC4388+vicinity"] = "pix_list=-13"

# no pars3, only bank=0 was observed

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, sys.argv)
