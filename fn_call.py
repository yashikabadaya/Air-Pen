from st1 import tr_data, tst_data 
from st3 import final_set, tst_final_set 
import threshCalculation
import predictionAndDisplay
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from fastdtw import fastdtw 
from sklearn.model_selection import LeaveOneOut
import numpy as np


training_data=tr_data()
# print(training_data)
count_of_unique_elements=len(training_data.label.unique())-1
# print(training_data.label.unique())
# print(count_of_unique_elements)
testing_data=tst_data()
# # # print(testing_data)
x_train,y_train=final_set(training_data)
# # # print(x_train)
x_test = tst_final_set(testing_data)



# print(y_train)
#count_of_unique_elements will be perfect when app is appending
t=threshCalculation.thres_per_gesture(x_train, y_train, count_of_unique_elements) 
th_gest=t._dist_matrix(x_train,y_train)
print(th_gest)


X_tr=np.array(x_train)
y_tr=np.array(y_train)

x_test=np.array(x_test)


p= predictionAndDisplay.knn_dtw(1,X_tr, y_tr, th_gest)

p.predict(x_test)


  
  
  

  
