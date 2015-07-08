

import numpy as np
import pandas as pd
from Mscthesis.Retrieve import *
from Mscthesis.Preprocess import Aggregator


locs = np.random.random((10000, 2))
Neigh = GridNeigh(locs, (100,100), (0, 1), (0, 1))

typevars = {'loc_vars':['x', 'y'], 'feat_vars': ['a'], 'agg_var':None}
agg = Aggregator(typevars=typevars, vals=[range(100), range(100)])

dflocs = pd.DataFrame(locs, columns=['x', 'y'])
dftype = pd.DataFrame(np.random.randint(0, 20,10000), columns=['a'])
df = pd.concat([dflocs, dftype], axis=1)

reindices = np.zeros((10000, 10+1))
reindices[:, 0] = np.arange(10000)
for i in range(10):
    reindices[:, i] = np.random.permutation(np.arange(10000))


Neigh = GridNeigh(locs, (100,100), (0, 1), (0, 1))
Neigh.define_aggretriever(agg, df, reindices)
Neigh.define_mainretriever(df, ['x', 'y'])

