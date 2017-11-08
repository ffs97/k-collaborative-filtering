#%%

root = "/home/fat-fighter/Documents/cs771-project/"

#%%

import sys
sys.path.append(root + "hybrid-method/")

#%%

from processing import extractFeaturesForSongs

extractFeaturesForSongs(root)

#%%
