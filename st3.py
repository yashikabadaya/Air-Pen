from st2 import start_and_end_pts
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsRegressor


columns=['label', 'x_acc','y_acc', 'z_acc','x_gyro', 'y_gyro', 'z_gyro','timestamp' ]
tst_columns=['x_acc','y_acc', 'z_acc','x_gyro', 'y_gyro', 'z_gyro','timestamp' ]


def final_set(training_data):
  final_training_set=pd.DataFrame(columns=['label', 'x_acc','y_acc', 'z_acc','x_gyro', 'y_gyro', 'z_gyro','timestamp' ])
  training_data, d = start_and_end_pts(training_data)

  # print(d)
  target=[]
  for m in range(len(d)):
  
    count_of_original_subset = training_data[d[m][0]:d[m][1]+1]['timestamp'].count()
    # print(k)
    df= pd.DataFrame(columns=['label', 'x_acc','y_acc', 'z_acc','x_gyro', 'y_gyro', 'z_gyro' ,'timestamp'])
    last_valid_index_of_subset= training_data[d[m][0]:d[m][1]+1]['timestamp'].last_valid_index()

  #   print(last_valid_index_of_subset)

    new_timestamp=[]
    c= (training_data[d[m][0]:d[m][1]+1]['timestamp'][last_valid_index_of_subset])
  
    new_timestamp.append(int(c) + 502)

    i=0
    labels_1=[training_data['label'][last_valid_index_of_subset]]
    for j in range(count_of_original_subset+2, 16):
      new_timestamp.append(new_timestamp[i]+502)
      labels_1.append(labels_1[i])
      i=i+1


    df=pd.DataFrame({'label':labels_1,'timestamp': new_timestamp})
    df.index=np.arange(last_valid_index_of_subset+1, len(df)+last_valid_index_of_subset+1)

    final_set=training_data[d[m][0]:d[m][1]+1].append(df)
    target.append(final_set['label'].values)

    # print(final_set)


    ###USING KNN REGRESSOR TO FIND VALUES OF NAN IN TRAINING SET

    #returns last index of the set


    total_count= final_set['timestamp'].last_valid_index()
  #   print(total_count)


    for j in range(len(columns)-1):
      last_index= final_set[columns[j+1]].last_valid_index()
  #     print(last_index)

      for i in range(0, (total_count- last_index) ):
  #       print(i)
  #       print(final_set[columns[j+1]].last_valid_index()+1)
  #       print(final_set[columns[j+1]].first_valid_index())
        X=np.array(final_set['timestamp'][:count_of_original_subset+i])
        X=X.reshape(-1,1)
        # print(X)
        Y=(np.array(final_set[columns[j+1]][:count_of_original_subset+i]))
        Y=Y.reshape(-1,1)
        Y=Y.astype(np.float)
        # print(Y)
        neigh = KNeighborsRegressor(n_neighbors=3)
        neigh.fit(X,Y)

        abc=final_set['timestamp'][final_set[columns[j+1]].last_valid_index()+1]
    

        final_set.at[final_set[columns[j+1]].last_valid_index()+1, columns[j+1]]=(neigh.predict([[abc]]))
   


    # print(final_set)
    final_training_set=final_training_set.append(final_set, ignore_index=True)
  #   print(final_training_set.last_valid_index())

    final_training_set.at[final_training_set['timestamp'].last_valid_index()+1, 'timestamp']='***'


  final_training_set= final_training_set[['x_acc', 'y_acc', 'z_acc','x_gyro','y_gyro', 'z_gyro']]

#   display(final_training_set)
  # print(target)
  training_set = np.array(list(final_training_set.values))
  
#   print(training_set.shape)
  
#   print(training_set)
  
  #CREATING SCALED DATA (Z NORMALIZATION)
  final_scaled_training_data=[]
  arr_to_be_scaled=[]
  for i in training_set:
#     i=np.array(i)
#     print(i)
    if np.isnan(i).any()== False:
      arr_to_be_scaled.append(i)
#       print(arr_to_be_scaled)
    if np.isnan(i).any()== True:
      scaled_data= preprocessing.scale(arr_to_be_scaled)
      final_scaled_training_data.append(scaled_data)
      arr_to_be_scaled=[]

  
  
  
  
  final_scaled_training_data=np.array(final_scaled_training_data)




  s=final_scaled_training_data.shape
#   print(s)
# final_scaled_training_data= final_scaled_training_data.reshape((s[0]*s[1],s[2]))
#   print(final_scaled_training_data)
  
  
  
  target=np.array(target)
#   print(target.shape)
#   print(target)
  # print(6666666666666)
  # print(final_scaled_training_data)

  return(final_scaled_training_data, target)





def tst_final_set(training_data):
  final_training_set=pd.DataFrame(columns=['x_acc','y_acc', 'z_acc','x_gyro', 'y_gyro', 'z_gyro','timestamp' ])
  # print(training_data)
  # training_data, d = start_and_end_pts(training_data)

  d=[[0,training_data.shape[0]]]
 
  for m in range(len(d)):

    count_of_original_subset = training_data[d[m][0]:d[m][1]+1]['timestamp'].count()
    # print(k)
    df= pd.DataFrame(columns=[ 'x_acc','y_acc', 'z_acc','x_gyro', 'y_gyro', 'z_gyro' ,'timestamp'])
    last_valid_index_of_subset= training_data[d[m][0]:d[m][1]+1]['timestamp'].last_valid_index()

  #   print(last_valid_index_of_subset)

    new_timestamp=[]
    c= (training_data[d[m][0]:d[m][1]+1]['timestamp'][last_valid_index_of_subset])

    new_timestamp.append(int(c) + 502)

    i=0
    # labels_1=[training_data['label'][last_valid_index_of_subset]]
    for j in range(count_of_original_subset+2, 16):
      new_timestamp.append(new_timestamp[i]+502)
      # labels_1.append(labels_1[i])
      i=i+1


    df=pd.DataFrame({'timestamp': new_timestamp})
    df.index=np.arange(last_valid_index_of_subset+1, len(df)+last_valid_index_of_subset+1)

    final_set=training_data[d[m][0]:d[m][1]+1].append(df)
    # target.append(final_set['label'].values)

    # print(final_set)


    ###USING KNN REGRESSOR TO FIND VALUES OF NAN IN TEST SET

    #returns last index of the set


    total_count= final_set['timestamp'].last_valid_index()
  #   print(total_count)


    for j in range(len(columns)-1):
      last_index= final_set[columns[j+1]].last_valid_index()
  #     print(last_index)

      for i in range(0, (total_count- last_index) ):

        X=np.array(final_set['timestamp'][:count_of_original_subset+i])
        X=X.reshape(-1,1)
        # print(X)
        Y=(np.array(final_set[columns[j+1]][:count_of_original_subset+i]))
        Y=Y.reshape(-1,1)
        Y=Y.astype(np.float)
        # print(Y)
        neigh = KNeighborsRegressor(n_neighbors=3)
        neigh.fit(X,Y)

    
        abc=final_set['timestamp'][final_set[columns[j+1]].last_valid_index()+1]
   

        final_set.at[final_set[columns[j+1]].last_valid_index()+1, columns[j+1]]=(neigh.predict([[abc]]))


    # print(final_set)
    final_training_set=final_training_set.append(final_set, ignore_index=True)
  #   print(final_training_set.last_valid_index())

    final_training_set.at[final_training_set['timestamp'].last_valid_index()+1, 'timestamp']='***'


  final_training_set= final_training_set[['x_acc', 'y_acc', 'z_acc','x_gyro','y_gyro', 'z_gyro']]

#   display(final_training_set)
  # print(target)
  training_set = np.array(list(final_training_set.values))
  
#   print(training_set.shape)
  
#   print(training_set)
  
  #CREATING SCALED DATA (Z NORMALIZATION)
  final_scaled_training_data=[]
  arr_to_be_scaled=[]
  for i in training_set:
#     i=np.array(i)
#     print(i)
    if np.isnan(i).any()== False:
      arr_to_be_scaled.append(i)
#       print(arr_to_be_scaled)
    if np.isnan(i).any()== True:
      scaled_data= preprocessing.scale(arr_to_be_scaled)
      final_scaled_training_data.append(scaled_data)
      arr_to_be_scaled=[]

  
  
  
  
  final_scaled_training_data=np.array(final_scaled_training_data)




  s=final_scaled_training_data.shape


  return(final_scaled_training_data)
