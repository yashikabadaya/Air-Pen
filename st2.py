#FOR FINDING STARTING AND END POINT IN DATA
# c contains i before every nan


def start_and_end_pts(training_data):
  # training_data= remove_ms_from_timestamp(training_data)
#   print(training_data)
  c=[0]
  for i in range(0, len(training_data)):
      if(training_data.iloc[i]['label']=="***" or training_data.iloc[i]['label']==" ***" ):
        c.append(i)  
        continue  
  #     else:
  #       print (training_data.iloc[i]['timestamp'],training_data.iloc[i]['x_acc'], training_data.iloc[i]['y_acc'], training_data.iloc[i]['z_acc'], training_data.iloc[i]['mean_acc'],training_data.iloc[i]['x_gyro'],training_data.iloc[i]['y_gyro'], training_data.iloc[i]['z_gyro'])

  # print(c)  
  # print(8888888)
  d=[]
  for i in range(len(c)-1):
    d.append([c[i]+1,c[i+1]-1])

  # print(d)  
  d[0][0]=0
  # print(d)
  return(training_data, d)
  