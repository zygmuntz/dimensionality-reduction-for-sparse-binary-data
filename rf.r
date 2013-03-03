# train a random forest on original or transformed data

library( randomForest )
library( caTools )

ntrees = 100

# change the file names
train_file = 'data/train.csv'
validation_file = 'data/test.csv'
label_index = 1

train <- read.csv( train_file, header = F )
validation <- read.csv( validation_file, header = F )

x_train = train[, -label_index]
y_train = train[, label_index]

x_validation = validation[, -label_index]
y_validation = validation[, label_index]

###

rf <- randomForest( x_train, as.factor( y_train ), ntree = ntrees, do.trace = 1 ) 

p <- predict( rf, x_validation, type = 'prob' )
probs =  p[,2]

p_binary <- predict( rf, validation[,-1] )

accuracy = sum( p_binary == y_validation ) / length( p_binary )
cat( "accuracy:", accuracy, "\n" )

auc = colAUC( probs, ( y_validation + 1 ) / 2 )
auc = auc[1]
cat( "auc:", auc, "\n" )

