# %% packages

import librosa.display
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

print("------- packages loaded ---------------")

# %%

# Import functions
from src.relative_mode import Tonal_Fragment
from src.relative_mode import relative_mode
from src.relative_mode import RME_across_time

#from src.relative_mode_across_time import RME_across_time

print("------- functions loaded ---------------")

## get an example
filename = 'data/Bach_1_Gould_0_Major_bachGould1971.wav'
y, sr = librosa.load(filename)
# %%

print("------- relative mode estimation ---------------")

x1, x2 = relative_mode(y=y, sr=sr, profile='simple')
print(x1.tondeltamax)
print(x2.tondeltamax)
# %%
print("------- relative mode estimation across time ---------------")

fig, x3 = RME_across_time(filename=filename, winlen=3, hoplen=3, cropfirst=0, croplast=0, chromatype='CENS', profile='albrecht',distance='cosine', plot=True)

#print(x3)
fig
plt.show()
