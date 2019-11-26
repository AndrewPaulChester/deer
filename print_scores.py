

from joblib import hash, dump, load
from matplotlib import pyplot as plt

fname = '/home/achester/Documents/DRL/deer/scores/test_6bf0bb50133fb6a38e16350e82465453aa03f606_scores.jldump'
scores = load(fname)
print (scores)
plt.plot(range(1, len(scores['vs'])+1), scores['vs'], label="VS", color='b')
plt.legend()
plt.xlabel("Number of epochs")
plt.ylabel("Score")
plt.savefig("scores.pdf")
plt.show()
