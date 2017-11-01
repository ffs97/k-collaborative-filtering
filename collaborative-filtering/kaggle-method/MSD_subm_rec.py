import sys
import MSD_util, MSD_rec

user_min, user_max, osfile = sys.argv[1:]
user_min = int(user_min)
user_max = int(user_max)

print "user_min: %d , user_max: %d" % (user_min, user_max)
sys.stdout.flush()

# TRIPLETS
f_triplets_tr = "train_triplets.txt"
f_triplets_tev = "kaggle_visible_evaluation_triplets.txt"

print 'loading users in %s' % "kaggle_users.txt"
sys.stdout.flush()
users_v = list(MSD_util.load_users("kaggle_users.txt"))
print len(users_v)

print 'default ordering by popularity'
sys.stdout.flush()
songs_ordered = MSD_util.sort_dict_dec(MSD_util.song_to_count(f_triplets_tr))

print "loading unique users indexes"
uu = MSD_util.unique_users(f_triplets_tr)
u2i = {}
for i, u in enumerate(uu):
    u2i[u] = i

print 'song to users on %s' % f_triplets_tr
s2u_tr = MSD_util.song_to_users(f_triplets_tr)

print "converting users to indexes"
for s in s2u_tr:
    s_set = set()
    for u in s2u_tr[s]:
        s_set.add(u2i[u])
    s2u_tr[s] = s_set

del u2i

print 'user to songs on %s' % f_triplets_tev
u2s_v = MSD_util.user_to_songs(f_triplets_tev)

print 'Creating predictor..'

_A = 0.15
_Q = 3
### calibrated
### pr=MSD_rec.PredSIc(s2u_tr, _A, _Q, "songs_scores.txt")

### uncalibrated
pr = MSD_rec.PredSI(s2u_tr, _A, _Q)

print 'Creating recommender..'
cp = MSD_rec.SReco(songs_ordered)
cp.Add(pr)
cp.Gamma = [1.0]

r = cp.RecommendToUsers(users_v[user_min:user_max], u2s_v)
MSD_util.save_recommendations(r, "kaggle_songs.txt", osfile)
