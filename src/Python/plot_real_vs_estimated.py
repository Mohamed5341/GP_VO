#!/usr/bin/env python

from pandas import *
import matplotlib.pyplot as plt
import math

filename1 = "models.csv"
filename2 = "svo.csv"

file1 = read_csv(filename1)
file2 = read_csv(filename2)

time_model = file1['%time'].tolist()
x_model = file1['field.pose2.position.x'].tolist()
y_model = file1['field.pose2.position.y'].tolist()
z_model = file1['field.pose2.position.z'].tolist()
qx_model = file1['field.pose2.orientation.x'].tolist()
qy_model = file1['field.pose2.orientation.y'].tolist()
qz_model = file1['field.pose2.orientation.z'].tolist()
qw_model = file1['field.pose2.orientation.w'].tolist()

time_svo = file2['%time'].tolist()
x_svo = file2['field.pose.position.x'].tolist()
y_svo = file2['field.pose.position.y'].tolist()
z_svo = file2['field.pose.position.z'].tolist()
qx_svo = file2['field.pose.orientation.x'].tolist()
qy_svo = file2['field.pose.orientation.y'].tolist()
qz_svo = file2['field.pose.orientation.z'].tolist()
qw_svo = file2['field.pose.orientation.w'].tolist()


#x_svo = [i * 3 + 1 for i in x_svo]
#y_svo = [i * 3 + 1 for i in y_svo]

start_time = max(time_model[0], time_svo[0])
end_time = min(time_model[-1], time_svo[-1])


for t in time_model:
    if(t >= start_time):
        model_start_i = time_model.index(t)
        break
for t in time_model[::-1]:
    if(t <= end_time):
        model_end_i = time_model.index(t)
        break

for t in time_svo:
    if(t >= start_time):
        svo_start_i = time_svo.index(t)
        break
for t in time_svo[::-1]:
    if(t <= end_time):
        svo_end_i = time_svo.index(t)
        break


time_model = time_model[model_start_i:model_end_i]
x_model = x_model[model_start_i:model_end_i]
y_model = y_model[model_start_i:model_end_i]
z_model = z_model[model_start_i:model_end_i]
qx_model = qx_model[model_start_i:model_end_i]
qy_model = qy_model[model_start_i:model_end_i]
qz_model = qz_model[model_start_i:model_end_i]
qw_model = qw_model[model_start_i:model_end_i]

time_svo = time_svo[svo_start_i:svo_end_i]
x_svo = x_svo[svo_start_i:svo_end_i]
y_svo = y_svo[svo_start_i:svo_end_i]
z_svo = z_svo[svo_start_i:svo_end_i]
qx_svo = qx_svo[svo_start_i:svo_end_i]
qy_svo = qy_svo[svo_start_i:svo_end_i]
qz_svo = qz_svo[svo_start_i:svo_end_i]
qw_svo = qw_svo[svo_start_i:svo_end_i]

x_svo_0 = x_svo[0]
y_svo_0 = y_svo[0]
x_svo = [((x-x_svo_0)*3.5) for x in x_svo]
y_svo = [(-(y-y_svo_0)*3.5) for y in y_svo]

x_model_0 = x_model[0]
y_model_0 = y_model[0]
x_model = [x - x_model_0 for x in x_model]
y_model = [y - y_model_0 for y in y_model]

plt.plot(x_model, y_model, label = 'True Position')
plt.plot(x_svo, y_svo, label = 'Estimated Position')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Actual vs Estimated position')
plt.legend()

plt.show()