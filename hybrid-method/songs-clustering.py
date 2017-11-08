import pandas as pd


columns = ["id", "k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10"]
cluster_columns = ["k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10"]

subset = False

for cov_type in ["spherical"]:
	print cov_type
	
	path = cov_type + "-songs-timbres-cluster-probabilities.csv"
	if subset:
		path = "data/subset/" + path
	else:
		path = "data/" + path
	timbres_probs = pd.read_csv(path, sep="\t")
	
	timbres_probs.columns = columns

	timbres_probs = timbres_probs.groupby("id").sum().reset_index()

	timbres_probs_ids = timbres_probs["id"]
	timbres_probs_data = timbres_probs[cluster_columns].div(timbres_probs[cluster_columns].sum(axis=1), axis=0)

	songs_cluster_probabilites = pd.concat([timbres_probs_ids, timbres_probs_data], axis=1)
	songs_cluster_probabilites.to_csv("data/" + cov_type + "-songs-cluster-probabilites.csv", sep="\t", index=False)
