## Abstract

The problem of recommendation systems is perhaps the most upfront application of
machine learning in the world. With the digital market comprising of over 50% of
the recording industry, the problem of music recommendation systems has become
more relevant over the years. With the right recommendation systems, firms can
attract more users which means higher revenue. Almost all streaming services
such as Apple Music, Spotify, Google Play Music, etc. use recommendation systems
to provide new song recommendations to their users.

There are multiple approaches to Music Reccomendation Systems, each exploited by
different streaming services.

* Neighbourhood Models such as Collaborative Filtering
* Content based ranking

Services such as Last.fm, Pandora, Spotify, etc. have successfully applied these
strategies to 

http://www.ifpi.org/facts-and-stats.php
https://papers.nips.cc/paper/5004-deep-content-based-music-recommendation.pdf
https://www.eecs.qmul.ac.uk/~simond/pub/2012/Song-Dixon-Pearce-CMMR-2012.pdf

### Approaches to MRS

#### Metadata based

**Limitations:** Does not expose users to much of new music, which fails the
complete purpose.

**Uses:** Fast and easy to implement. Can be used as a prior to the user
modelling part. Apple music does this.

#### MIR

* User Profiling
* Feature Retrieval and Selection
* Mapping User Features to Music Features and providing suggestions

**Limitations:** Difficult to extract and retrieve features. [Music Genome
Project is an example]. Difficult to provide suggestions. Tradeoff between speed
and variety (not clustering might break genre barriers)

**Uses:** Can be very helpful in giving on the fly suggestions based on current
music buffer (like the station feature in Apple Music)

**Approach:** Adding current user features such as mood, and providing
suggestions from new clusters rather than just using nearest neighbours
approach.


#### Collaborative Filtering

This approach provides extremely good results as proven by Netflix. Spotify also
uses.

Does not involve many steps other than modelling. Factor models can be used.

**Limitations:** Cold Start problem

**Uses:** Netflix proved that this is indeed a very good step to providing
suggestions. However the similarity of users when providing music suggestions
has not been proven.
