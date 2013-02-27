import sys, time
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
print

c = SvmLightCorpus( input_file )

print "running LDA..."
print time.strftime("%H:%M:%S", time.localtime())
print

lda = models.LdaModel( c, id2word = None, num_topics = num_topics )

print "converting corpus to LDA..."
print time.strftime("%H:%M:%S", time.localtime())
print

c_lda = lda[c] 

print "saving..."
print

SvmLightCorpus.serialize( output_file, c_lda  )

print "done."
print time.strftime("%H:%M:%S", time.localtime())