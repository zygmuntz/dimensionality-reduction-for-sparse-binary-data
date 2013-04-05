'map input file (libsvm) to <argv[3]> topics, output csv'

from sklearn.datasets import load_svmlight_file
import numpy as np
import spams
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
try:
	num_topics = int( sys.argv[3] )
except IndexError:
	num_topics = 50

x_train, y_train = load_svmlight_file( input_file )
x_train_t = np.transpose( x_train )

u = spams.nmf( x_train_t, return_lasso = False, K = num_topics )

mapped_x = x_train * u

y_train.shape = y_train.shape[0], 1
np.savetxt( output_file, np.hstack(( y_train, mapped_x )), delimiter = ",", fmt = '%.6f' )
