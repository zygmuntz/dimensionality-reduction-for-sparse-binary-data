import time, sys
from gensim import corpora, models, similarities
from gensim.corpora import SvmLightCorpus

input_file = sys.argv[1]
output_file = sys.argv[2]
try:
	num_topics = int( sys.argv[3] )
except IndexError:
	num_topics = 50

###

print "loading data..."
print time.strftime("%H:%M:%S", time.localtime())

c = SvmLightCorpus( input_file )

print "starting tf-idf..."
print

tfidf = models.TfidfModel( c )
c_tfidf = tfidf[c]

print "running RP..."
print time.strftime("%H:%M:%S", time.localtime())
print

rp = models.RpModel( c_tfidf, num_topics = num_topics )

print "converting corpus to RP..."
print time.strftime("%H:%M:%S", time.localtime())

c_rp = rp[c_tfidf] 

print "saving..."
print

SvmLightCorpus.serialize( output_file, c_rp  )

print "done."
print time.strftime("%H:%M:%S", time.localtime())
