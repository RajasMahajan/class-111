import plotly.figure_factory as ff 
import csv
import pandas as pd 
import statistics
import random 
import plotly.graph_objects as go 


df=pd.read_csv("school2.csv")
data=df["Math_score"].tolist()


fig= ff.create_distplot([data],["Math Score"],show_hist=False)
fig.show()

mean=statistics.mean(data)
std=statistics.stdev(data)
# print(mean,std)

def random_counter(counter):
    dataset=[]
    for i in range(0,counter):
        rindex=random.randint(0,len(data)-1)
        value=data[rindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean 



mean_list=[]
for i in range(0,1000):
    set_of_values=random_counter(100)
    mean_list.append(set_of_values)

mean=statistics.mean(mean_list)
std= statistics.stdev(mean_list)
print(mean,std)

first_std_dev_start,first_std_dev_end=mean-std,mean+std
second_std_dev_start,second_std_dev_end=mean-(std*2),mean+(std*2)
third_std_dev_start,third_std_dev_end=mean-(std*3),mean+(std*3)


'''
fig= ff.create_distplot([mean_list],["Math Score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_dev_end,first_std_dev_end],y=[0,0.20],mode="lines",name="First Standard Deviation at end"))
fig.add_trace(go.Scatter(x=[second_std_dev_end,second_std_dev_end],y=[0,0.20],mode="lines",name="Second Standard Deviation at end"))
fig.add_trace(go.Scatter(x=[third_std_dev_end,third_std_dev_end],y=[0,0.20],mode="lines",name = "Third Standard Deviation at end"))
fig.add_trace(go.Scatter(x=[first_std_dev_start,first_std_dev_start],y=[0,0.20],mode="lines",name="First Standard Deviation at start"))
fig.add_trace(go.Scatter(x=[second_std_dev_start,second_std_dev_start],y=[0,0.20],mode="lines",name="Second Standard Deviation at start"))
fig.add_trace(go.Scatter(x=[third_std_dev_start,third_std_dev_start],y=[0,0.20],mode="lines",name = "Third Standard Deviation at start"))
fig.show()
'''
'''
df=pd.read_csv("school_sample1.csv")
data=df["Math_score"].tolist()
mean_sample1=statistics.mean(data)
fig= ff.create_distplot([mean_list],["Math Score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_sample1,mean_sample1],y=[0,0.20],mode="lines",name="future_mean_of_data1"))
fig.add_trace(go.Scatter(x=[first_std_dev_end,first_std_dev_end],y=[0,0.20],mode="lines",name="First Standard Deviation at end"))
fig.show()
'''
df=pd.read_csv("school_sample2.csv")
data=df["Math_score"].tolist()
mean_sample2=statistics.mean(data)
fig= ff.create_distplot([mean_list],["Math Score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_sample2,mean_sample2],y=[0,0.20],mode="lines",name="future_mean_of_data2"))
fig.add_trace(go.Scatter(x=[second_std_dev_end,second_std_dev_end],y=[0,0.20],mode="lines",name="First Standard Deviation at end"))
fig.show()

# print((first_std_dev_end/mean_sample1)*100)
'''
df=pd.read_csv("school_sample3.csv")
data=df["Math_score"].tolist()
mean_sample3=statistics.mean(data)
fig= ff.create_distplot([mean_list],["Math Score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_sample3,mean_sample3],y=[0,0.20],mode="lines",name="future_mean_of_data3"))
fig.add_trace(go.Scatter(x=[third_std_dev_end,third_std_dev_end],y=[0,0.20],mode="lines",name="First Standard Deviation at end"))
fig.show()
'''
z_score=(mean_sample2-mean)/std
print(z_score)


