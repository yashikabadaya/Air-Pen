#CALCULATING THRESHOLD
#n= total number of gestures in the vocab
import numpy as np
from fastdtw import fastdtw
from sklearn.metrics import f1_score
from scipy.spatial.distance import euclidean
class thres_per_gesture():
  def __init__ (self, x_train, y_train,n):
    self.x_train=x_train
    self.y_train=y_train
    self.n=n

    
  def dtw(self,x,y):
    distance, path = fastdtw(x, y, dist=euclidean)
    return(distance)
  
  def condition_gest(self,y,gest,dm,i,j,k):
    for c in range(0,self.n):
      if( y[i][0]== c ):

        gest[str(k)+str(c)].append(dm[j][i])
        # print(gest[str(k)+str(c)])

  def condition_best_thresh(self,a,gest,k):
    for c in range(0,self.n):

      a[str(k)+str(c)]=(gest[str(k)+str(c)][1])
      
  def condition_worst_thresh(self,a,gest,k):
    for c in range(0,self.n):
  
      a[str(k)+str(c)]=(max(gest[str(k)+str(c)]))

  
  def _dist_matrix ( self , x ,y):
    y_train=y 
    y=[]
    y_train=list(y_train)
    # print(y_train)
    for i in range( len(y_train)):
      y.append(list(map(int, y_train[i])))
    y=np.array(y)
    # print(y)
    dm_count = 0
#x_s and y_s are x trains and y_train resp
#x_s[0] is 20
    x_s = np.shape(x)   
    y_s = np.shape(y)

    dm = np.zeros((x_s[0], x_s[0])) 
    dm_size = x_s[0]*x_s[0]
# 00-HH, 01-HV, 10-VH, 11-VV
    
    gest={}  
    for i in range(0,self.n):
      for j in range(0,self.n):
        gest[str(i)+str(j)]=[]
    # gest={'00':[], '11': [],'22':[], '10':[], '01':[],'02':[],'12':[],'20':[],'21':[]}
#dm calculation
    for i in range(0, x_s[0]):
        for j in range(0, x_s[0]):
            dm[i, j] = self.dtw(x[i],x[j])
            dm_count += 1

    # print(dm)
    best_thresh=[]
    worst_thresh=[]
    
    for j in range(0,x_s[0]):     
#       print(y[j][0])
 
      for i in range(0,x_s[0]):
        for k in range (0,self.n):
          if (y[j][0]==k):
            self.condition_gest(y,gest,dm,i,j,k)

      try:   
        best_thresh.append([])
        a={}
        for m in range(0,self.n):
          for k in range(0,self.n):
              # print(gest[str(m)+str(k)])
              gest[str(m)+str(k)].sort()

        

        for k in range(0,self.n):
          if(y[j][0]==k):
            self.condition_best_thresh(a,gest,k)
 
        best_thresh[j].append(a)
        # print(best_thresh[j])

      except ValueError:
        pass

        # print(best_thresh)

      try:    
        worst_thresh.append([])
        a={}
        
        for k in range(0,self.n):
          if(y[j][0]==k):
            self.condition_worst_thresh(a,gest,k)
        
        worst_thresh[j].append(a)

      except ValueError:
        pass

     
      # print(best_thresh)

    th_gest={}
    for k in range(0,self.n):
      
      T=[]
      f_score=[]
      for i in range(0, x_s[0]):
        if (k == y[i][0]):
          
          #both same (j and gesture k)
          T.append(worst_thresh[i][0][str(k)+str(k)])
        else:
        # best_thresh array's jth element's gesture kth part
          # print(best_thresh[i])
          T.append(best_thresh[i][0][str(y[i][0])+str(k)])
      T.sort()
    #to loop through each element in T
      for i in range(len(T)):
    
        y_pred=[]
        y_true=[]
        #to loop through each row of dm
        for j in range(len(T)):
          index = np.argwhere(dm[j]==0.0)
          a=np.delete(dm[j],index[0][0])
          b=np.delete(y_train,index,axis=0)
#           print(b)
          knn_idx = a.argmin(axis=0)
#           print(knn_idx,a[knn_idx], T[i],b[knn_idx])

          if(a[knn_idx]<T[i]):
            knn_labels = b[knn_idx][0]
            y_pred.append(knn_labels)
            y_true.append(k)

        # print(y_true)
        # print(y_pred)
        y_pred=list(map(int, y_pred))
        a=f1_score(y_true, y_pred, average='micro')
#         print(a)
        f_score.append(a)
        
  

      th_gest[k]=T[f_score.index(max(f_score))]
      # print(max(f_score))
   
          
    return(th_gest)
  

  


