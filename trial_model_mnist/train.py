
#Notifies jupyter notebook not to run this portion but write it to a file, by providing path
#Creates a python file called train.py from the content of this block. 


# Import all relevant libraries
import argparse
import os
import numpy as np
import glob


from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

from sklearn.metrics import accuracy_score
from azureml.core import Run
# from utils import load_data

import gzip
import struct

# 1 load compressed MNIST gz files and return numpy arrays
def zip_to_array (filename, label=False):
    with gzip.open(filename) as gz:
        struct.unpack('I', gz.read(4))
        n_items = struct.unpack('>I', gz.read(4))
        if not label:
            n_rows = struct.unpack('>I', gz.read(4))[0]
            n_cols = struct.unpack('>I', gz.read(4))[0]
            res = np.frombuffer(gz.read(n_items[0] * n_rows * n_cols), dtype=np.uint8)
            res = res.reshape(n_items[0], n_rows * n_cols)
        else:
            res = np.frombuffer(gz.read(n_items[0]), dtype=np.uint8)
            res = res.reshape(n_items[0], 1)
    return res


# 2 let user feed in 2 parameters, the dataset to mount or download, and the regularization rate of the logistic regression model
parser = argparse.ArgumentParser()
parser.add_argument('--data-folder', type=str, dest='data_folder', help='data folder mounting point')
parser.add_argument('--reg-rate', type=float, dest='reg', default=0.01, help='regularization rate')
args = parser.parse_args() ###args is now made up of "args.data_folder" & "args.reg" which we will use later

# 3 Use zip_to_array function
###Extracts the data from our ws folder & stores it in the specified variobles X_train, X_test, y_train, y_test
###  "mnist" we created earlier & "args.data_folder" is one of the arguments we parse above
data_folder = os.path.join(args.data_folder, 'mnist')
print('Data folder:', data_folder) #just to see
# load the X train and test set into numpy arrays
X_train = zip_to_array(os.path.join(data_folder, 'train-images.gz'), False) / 255.0
X_test = zip_to_array(os.path.join(data_folder, 'test-images.gz'), False) / 255.0
print(X_train.shape, X_test.shape, sep = '\n') #print variable set dimension

# load the y train and test set into numpy arrays
y_train = zip_to_array(os.path.join(data_folder, 'train-labels.gz'), True).reshape(-1)
y_test = zip_to_array(os.path.join(data_folder, 'test-labels.gz'), True).reshape(-1)
print( y_train.shape, y_test.shape, sep = '\n') #print the response variable dimension


# 4 The Logistic regression model being called into action
####### Get hold of the current run for model scoring - 
########This is very important, as it can be used to store vital information about your model performance
run = Run.get_context()

#### This line creates an instance of the model, using the regularization rate that was passed earlier
print('Train a logistic regression model with regularization rate of', args.reg) #status update
Logreg = LogisticRegression(C=1.0/args.reg, solver="liblinear", multi_class="auto", random_state=42)
# Then we fit our train data to the model
Logreg.fit(X_train, y_train)

print('Predict the test set') #status update
y_hat = Logreg.predict(X_test) #prediction from our model

#print the accuracy
# calculate accuracy on the prediction
acc = accuracy_score(y_test, y_hat)
print('Accuracy is', acc)

# remember we ran a get_context function on our experiment, well, now we can log things in it
### Here we log regularization rate and accuracy
run.log('regularization rate', np.float(args.reg))
run.log('accuracy', np.float(acc))

# 5 Create a pickle file that stores our trained Logreg model & we can use later
# note file saved in the outputs folder is automatically uploaded into experiment record
### We can usse  pickle file to deploy model later
os.makedirs('outputs', exist_ok=True) #creates folder
print(os.getcwd()) ## just to confirm its the cloud computer - vm
joblib.dump(value=Logreg, filename='./outputs/sklearn_mnist_model.pkl') #creates the ".pkl" file
