import sys, time
from gensim import corpora, models, similarities
from gensim.corpora import SvmLightCorpus

input_file = sys.argv[1]
output_file = sys.argv[2]

###

print "loading data..."
print time.strftime("%H:%M:%S", time.localtime())

c = SvmLightCorpus( input_file )

print "starting tf-idf..."
print

tfidf = models.TfidfModel( c )
c_tfidf = tfidf[c]

print "saving..."
print

SvmLightCorpus.serialize( output_file, c_tfidf  )

print "done."
print time.strftime("%H:%M:%S", time.localtime())
