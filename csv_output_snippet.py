from gensim import matutils 

output_file = 'output.csv'

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html
numpy.savetxt( output_file, matutils.corpus2dense( transformed_corpus, num_cols ), fmt = '%.6f', delimiter = ',' )
