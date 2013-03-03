'convert libsvm file to csv'
'libsvm2csv.py <input file> <output file> <dimensionality>'

import sys, csv
#import numpy as np

input_file = sys.argv[1]
output_file = sys.argv[2]

d = int( sys.argv[3] )
assert ( d > 0 )

reader = csv.reader( open( input_file ), delimiter = " " )
writer = csv.writer( open( output_file, 'wb' ))

for line in reader:
	label = line.pop( 0 )
	if line[-1].strip() == '':
		line.pop( -1 )
		
	# print line
	
	line = map( lambda x: tuple( x.split( ":" )), line )
	#print line
	
	new_line = [ label ] + [ 0 ] * d
	for i, v in line:
		new_line[int(i)] = v
		
	writer.writerow( new_line )
