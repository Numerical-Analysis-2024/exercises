#!/usr/bin/env python

import numpy as np
from numpy.linalg import cond

A = np.array(object=[[1, 0, -1], [0, 1, 0], [1, 0, 1]])
conditions_number = [
    cond(x=A),
    cond(x=A, p="fro"),
    cond(x=A, p=np.inf),
    cond(x=A, p=-np.inf),
    cond(x=A, p=1),
    cond(x=A, p=-1),
    cond(x=A, p=2),
]

print(f"Severals condition numbers:\n{str(conditions_number)[1:-1]}")
