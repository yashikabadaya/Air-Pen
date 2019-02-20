import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
from tkinter import *
import os
import pyttsx3
import threading
from threading import Thread


###GESTURE MATCHING
class knn_dtw():

    def  __init__  (self, n_neighbors , x_train, y_train, th_gest):
      self.n_neighbors= n_neighbors
      self.x_train= x_train
      self.y_train= y_train
      self.th_gest =th_gest


   #it will take in each observation ie. x and y will be of form [x_acc, y_acc, z_acc, x_gyro, y_gyro, z_gyro]
   #x= array from x_train and y= array from x_test

    def dtw(self,x,y):
     
      distance, path = fastdtw(x, y, dist=euclidean)

      return(distance)
      

  #x= x_train, y= x_test
    def _dist_matrix ( self , x ,y):
      dm_count = 0
      
    
      if(np.array_equal(x, y)):
          x_s = np.shape(x)
          dm = np.zeros((x_s[0] * (x_s[0] - 1)) // 2, dtype=np.double)


          for i in range(0, x_s[0] - 1):
              for j in range(i + 1, x_s[0]):
                  dm[dm_count] = self.dtw(x[i],y[j])
                  dm_count += 1

        
          return dm

      # Compute full distance matrix of dtw distnces between x and y

      else:
# x= x_test and y is x_train

          x_s = np.shape(x)
          
          y_s = np.shape(y)
          
          dm = np.zeros((x_s[0], y_s[0])) 
          dm_size = x_s[0]*y_s[0]


          for i in range(0, x_s[0]):
              for j in range(0, y_s[0]):
                  dm[i, j] = self.dtw(x[i],y[j])
                  dm_count += 1

          return dm



#x is the testing data

    def predict(self, x_test):
    
      dm = self._dist_matrix(x_test,self.x_train)
#       print(dm)
      knn_idx = dm[0].argmin()
      # print(knn_idx)
      # print(dm[0][knn_idx])
      
      knn_labels = np.array(self.y_train[knn_idx])
      # print(knn_labels)
      knn_labels=list(map(int, knn_labels))
      # print(knn_labels[0])
      
      d={}
      with open("vocab.txt") as f:
        for line in f:
          (key,value)=line.split()
          d[key]=value
      # print(d)
      
      if(dm[0][knn_idx]<=self.th_gest[knn_labels[0]]):
          print("Predicted:",d.get(str(knn_labels[0])))


###DISPLAY THE RESULT
          def display():
            root=Tk()
            root.geometry('1380x720')
            root.title("PREDICTION RESULT")
            lab1=Label(root,text=d.get(str(knn_labels[0])),bd=1,font='times 100',width=29440,height=45000).pack()
            root.config(background='white')
            root.mainloop()



          def tts():
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate-40)
            engine.say(d.get(str(knn_labels[0])))
            engine.runAndWait()


          
          Thread(target = display).start()
          Thread(target = tts).start()


         



      else:
   
        def display_1():
            root=Tk()
            root.geometry('1380x720')
            root.title("PREDICTION RESULT")
            lab1=Label(root,text="Gesture is not in vocabulary.",bd=1,font='times 100',width=29440,height=45000).pack()
            root.config(background='white')
            root.mainloop()



        def tts_1():
          engine = pyttsx3.init()
          voices = engine.getProperty('voices')
          engine.setProperty('voice', voices[1].id)
          rate = engine.getProperty('rate')
          engine.setProperty('rate', rate-40)
          engine.say("Gesture is not in vocabulary.")
          engine.runAndWait()


        
        Thread(target = display_1).start()
        Thread(target = tts_1).start()