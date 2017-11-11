import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

from sklearn.mixture import GaussianMixture
from sklearn.model_selection import StratifiedKFold


timbres = pd.read_csv("data/songs-timbres.csv", sep="\t")

timbres_col_list = ["t1", "t2", "t3", "t4", "t5",
                    "t6", "t7", "t8", "t9", "t10", "t11", "t12"]
timbres_data = timbres[timbres_col_list]

n_clusters = 10
estimators = dict(
    (cov_type, GaussianMixture(
        n_components=n_clusters,
        covariance_type=cov_type,
        max_iter=1000,
        random_state=0))
    for cov_type in ['spherical', 'diag', 'tied'])


for index, (name, estimator) in enumerate(estimators.items()):
    print "Running GMM with covariance matrix type:", name
    estimator.fit(timbres_data)
    print "\tEstimator Learned"
    probs = estimator.predict_proba(timbres_data)
    with open("data/" + name + "-songs-timbres-cluster-probabilities.csv", "w") as f:
        for i, song_id in enumerate(timbres["id"]):
            params = [song_id]
            params.extend(probs[i])

            params = [str(param) for param in params]

            f.write("\t".join(params) + "\n")

    print "\tObserved AIC Value:", estimator.aic(timbres_data), "\n"
