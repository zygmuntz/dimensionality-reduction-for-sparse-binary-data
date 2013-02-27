'add labels from the original libsvm file after gensim conversion'

import sys, csv

original_file = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

orig_reader = csv.reader( open( original_file ), delimiter = ' ' )
reader = csv.reader( open( input_file ), delimiter = ' ' )
writer = csv.writer( open( output_file, 'wb' ), delimiter = ' ' )

n = 0
for line in orig_reader:
	label = line[0]
	
	line = reader.next()
	line[0] = label
	
	writer.writerow( line )
	
	n += 1
	if n % 10000 == 0:
		print n
