import pandas as pd
import os


 
def tr_data():
	columns_1=['label', 'x_acc','y_acc', 'z_acc','x_gyro', 'y_gyro', 'z_gyro', 'timestamp' ]
	columns=['label', 'x_acc','y_acc', 'z_acc','x_gyro', 'y_gyro', 'z_gyro','timestamp' ]

	training_data = pd.read_csv('traindata.txt', names= columns_1) 
	
	return (training_data)

def tst_data():
	columns_1=['label', 'x_acc','y_acc', 'z_acc','x_gyro', 'y_gyro', 'z_gyro', 'timestamp' ]
	columns=[ 'x_acc','y_acc', 'z_acc','x_gyro', 'y_gyro', 'z_gyro','timestamp' ]
	
	testing_data=pd.read_csv('testdata.txt',names=columns)
		
	return (testing_data)

