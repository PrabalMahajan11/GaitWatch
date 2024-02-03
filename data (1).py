# -*- coding: utf-8 -*-
"""data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qpi6ROaQmX7raOG8ft1hMOsU5jiUzyKv
"""

import json
import numpy as np
import csv

fileno = "S1"

inputs = []
labels = []

all_reading = []
with open(fileno+'L_normal.json', 'r') as json_file:
    with open(fileno+'R_normal.json','r') as json_file2:
        data1 = json.load(json_file)
        data1 = data1['UsersData']['GCeG0u1ovpfUxScbzJYcEKgp4bq2']['readings']
        data2 = json.load(json_file2)
        data2 = data2['UsersData']['edpU0psG0NfcTLhIRAF20sGM7w53']['readings']
        count = 30
        for (reading1,reading2) in zip(data1,data2):
            one_reading = []
            reading = data1[reading1]
            one_reading.append(reading['Accangle1']['x'])
            one_reading.append(reading['Accangle1']['y'])
            one_reading.append(reading['Accangle2']['x'])
            one_reading.append(reading['Accangle2']['y'])
            one_reading.append(reading['Acceleration1']['x'])
            one_reading.append(reading['Acceleration1']['y'])
            one_reading.append(reading['Acceleration1']['z'])
            one_reading.append(reading['Acceleration2']['x'])
            one_reading.append(reading['Acceleration2']['y'])
            one_reading.append(reading['Acceleration2']['z'])
            one_reading.append(reading['Angle1']['x'])
            one_reading.append(reading['Angle1']['y'])
            one_reading.append(reading['Angle1']['z'])
            one_reading.append(reading['Angle2']['x'])
            one_reading.append(reading['Angle2']['y'])
            one_reading.append(reading['Angle2']['z'])
            one_reading.append(reading['Gyro1']['x'])
            one_reading.append(reading['Gyro1']['y'])
            one_reading.append(reading['Gyro1']['z'])
            one_reading.append(reading['Gyro2']['x'])
            one_reading.append(reading['Gyro2']['y'])
            one_reading.append(reading['Gyro2']['z'])
            one_reading.append(reading['distance1'])
            one_reading.append(reading['distance2'])
            one_reading.append(reading['voltage0'])
            one_reading.append(reading['voltage1'])
            one_reading.append(reading['voltage2'])

            reading = data2[reading2]
            one_reading.append(reading['Accangle1']['x'])
            one_reading.append(reading['Accangle1']['y'])
            one_reading.append(reading['Accangle2']['x'])
            one_reading.append(reading['Accangle2']['y'])
            one_reading.append(reading['Acceleration1']['x'])
            one_reading.append(reading['Acceleration1']['y'])
            one_reading.append(reading['Acceleration1']['z'])
            one_reading.append(reading['Acceleration2']['x'])
            one_reading.append(reading['Acceleration2']['y'])
            one_reading.append(reading['Acceleration2']['z'])
            one_reading.append(reading['Angle1']['x'])
            one_reading.append(reading['Angle1']['y'])
            one_reading.append(reading['Angle1']['z'])
            one_reading.append(reading['Angle2']['x'])
            one_reading.append(reading['Angle2']['y'])
            one_reading.append(reading['Angle2']['z'])
            one_reading.append(reading['Gyro1']['x'])
            one_reading.append(reading['Gyro1']['y'])
            one_reading.append(reading['Gyro1']['z'])
            one_reading.append(reading['Gyro2']['x'])
            one_reading.append(reading['Gyro2']['y'])
            one_reading.append(reading['Gyro2']['z'])
            one_reading.append(reading['distance1'])
            one_reading.append(reading['distance2'])
            one_reading.append(reading['voltage0'])
            one_reading.append(reading['voltage1'])
            one_reading.append(reading['voltage2'])

            all_reading.append(one_reading)
            count = count-1
            if(count==0):
              break
        while(count>0):
          count -= 1
          one_reading = []
          for i in range(54):
            one_reading.append(0.0)
          all_reading.append(one_reading)


labels.append(0)
inputs.append(all_reading)
#----------------------------------------------------------------

all_reading = []
with open(fileno+'L_circum.json', 'r') as json_file:
    with open(fileno+'R_circum.json','r') as json_file2:
        data1 = json.load(json_file)
        data1 = data1['UsersData']['GCeG0u1ovpfUxScbzJYcEKgp4bq2']['readings']
        data2 = json.load(json_file2)
        data2 = data2['UsersData']['edpU0psG0NfcTLhIRAF20sGM7w53']['readings']
        count = 30
        for (reading1,reading2) in zip(data1,data2):
            one_reading = []
            reading = data1[reading1]
            one_reading.append(reading['Accangle1']['x'])
            one_reading.append(reading['Accangle1']['y'])
            one_reading.append(reading['Accangle2']['x'])
            one_reading.append(reading['Accangle2']['y'])
            one_reading.append(reading['Acceleration1']['x'])
            one_reading.append(reading['Acceleration1']['y'])
            one_reading.append(reading['Acceleration1']['z'])
            one_reading.append(reading['Acceleration2']['x'])
            one_reading.append(reading['Acceleration2']['y'])
            one_reading.append(reading['Acceleration2']['z'])
            one_reading.append(reading['Angle1']['x'])
            one_reading.append(reading['Angle1']['y'])
            one_reading.append(reading['Angle1']['z'])
            one_reading.append(reading['Angle2']['x'])
            one_reading.append(reading['Angle2']['y'])
            one_reading.append(reading['Angle2']['z'])
            one_reading.append(reading['Gyro1']['x'])
            one_reading.append(reading['Gyro1']['y'])
            one_reading.append(reading['Gyro1']['z'])
            one_reading.append(reading['Gyro2']['x'])
            one_reading.append(reading['Gyro2']['y'])
            one_reading.append(reading['Gyro2']['z'])
            one_reading.append(reading['distance1'])
            one_reading.append(reading['distance2'])
            one_reading.append(reading['voltage0'])
            one_reading.append(reading['voltage1'])
            one_reading.append(reading['voltage2'])

            reading = data2[reading2]
            one_reading.append(reading['Accangle1']['x'])
            one_reading.append(reading['Accangle1']['y'])
            one_reading.append(reading['Accangle2']['x'])
            one_reading.append(reading['Accangle2']['y'])
            one_reading.append(reading['Acceleration1']['x'])
            one_reading.append(reading['Acceleration1']['y'])
            one_reading.append(reading['Acceleration1']['z'])
            one_reading.append(reading['Acceleration2']['x'])
            one_reading.append(reading['Acceleration2']['y'])
            one_reading.append(reading['Acceleration2']['z'])
            one_reading.append(reading['Angle1']['x'])
            one_reading.append(reading['Angle1']['y'])
            one_reading.append(reading['Angle1']['z'])
            one_reading.append(reading['Angle2']['x'])
            one_reading.append(reading['Angle2']['y'])
            one_reading.append(reading['Angle2']['z'])
            one_reading.append(reading['Gyro1']['x'])
            one_reading.append(reading['Gyro1']['y'])
            one_reading.append(reading['Gyro1']['z'])
            one_reading.append(reading['Gyro2']['x'])
            one_reading.append(reading['Gyro2']['y'])
            one_reading.append(reading['Gyro2']['z'])
            one_reading.append(reading['distance1'])
            one_reading.append(reading['distance2'])
            one_reading.append(reading['voltage0'])
            one_reading.append(reading['voltage1'])
            one_reading.append(reading['voltage2'])

            all_reading.append(one_reading)
            count = count-1
            if(count==0):
              break
        while(count>0):
          count -= 1
          one_reading = []
          for i in range(54):
            one_reading.append(0.0)
          all_reading.append(one_reading)


labels.append(1)
inputs.append(all_reading)

# #----------------------------------------------------------------

all_reading = []
with open(fileno+'L_GM.json', 'r') as json_file:
    with open(fileno+'R_GM.json','r') as json_file2:
        data1 = json.load(json_file)
        data1 = data1['UsersData']['GCeG0u1ovpfUxScbzJYcEKgp4bq2']['readings']
        data2 = json.load(json_file2)
        data2 = data2['UsersData']['edpU0psG0NfcTLhIRAF20sGM7w53']['readings']
        count = 30
        for (reading1,reading2) in zip(data1,data2):
            one_reading = []
            reading = data1[reading1]
            one_reading.append(reading['Accangle1']['x'])
            one_reading.append(reading['Accangle1']['y'])
            one_reading.append(reading['Accangle2']['x'])
            one_reading.append(reading['Accangle2']['y'])
            one_reading.append(reading['Acceleration1']['x'])
            one_reading.append(reading['Acceleration1']['y'])
            one_reading.append(reading['Acceleration1']['z'])
            one_reading.append(reading['Acceleration2']['x'])
            one_reading.append(reading['Acceleration2']['y'])
            one_reading.append(reading['Acceleration2']['z'])
            one_reading.append(reading['Angle1']['x'])
            one_reading.append(reading['Angle1']['y'])
            one_reading.append(reading['Angle1']['z'])
            one_reading.append(reading['Angle2']['x'])
            one_reading.append(reading['Angle2']['y'])
            one_reading.append(reading['Angle2']['z'])
            one_reading.append(reading['Gyro1']['x'])
            one_reading.append(reading['Gyro1']['y'])
            one_reading.append(reading['Gyro1']['z'])
            one_reading.append(reading['Gyro2']['x'])
            one_reading.append(reading['Gyro2']['y'])
            one_reading.append(reading['Gyro2']['z'])
            one_reading.append(reading['distance1'])
            one_reading.append(reading['distance2'])
            one_reading.append(reading['voltage0'])
            one_reading.append(reading['voltage1'])
            one_reading.append(reading['voltage2'])

            reading = data2[reading2]
            one_reading.append(reading['Accangle1']['x'])
            one_reading.append(reading['Accangle1']['y'])
            one_reading.append(reading['Accangle2']['x'])
            one_reading.append(reading['Accangle2']['y'])
            one_reading.append(reading['Acceleration1']['x'])
            one_reading.append(reading['Acceleration1']['y'])
            one_reading.append(reading['Acceleration1']['z'])
            one_reading.append(reading['Acceleration2']['x'])
            one_reading.append(reading['Acceleration2']['y'])
            one_reading.append(reading['Acceleration2']['z'])
            one_reading.append(reading['Angle1']['x'])
            one_reading.append(reading['Angle1']['y'])
            one_reading.append(reading['Angle1']['z'])
            one_reading.append(reading['Angle2']['x'])
            one_reading.append(reading['Angle2']['y'])
            one_reading.append(reading['Angle2']['z'])
            one_reading.append(reading['Gyro1']['x'])
            one_reading.append(reading['Gyro1']['y'])
            one_reading.append(reading['Gyro1']['z'])
            one_reading.append(reading['Gyro2']['x'])
            one_reading.append(reading['Gyro2']['y'])
            one_reading.append(reading['Gyro2']['z'])
            one_reading.append(reading['distance1'])
            one_reading.append(reading['distance2'])
            one_reading.append(reading['voltage0'])
            one_reading.append(reading['voltage1'])
            one_reading.append(reading['voltage2'])

            all_reading.append(one_reading)
            count = count-1
            if(count==0):
              break
        while(count>0):
          count -= 1
          one_reading = []
          for i in range(54):
            one_reading.append(0.0)
          all_reading.append(one_reading)


labels.append(2)
inputs.append(all_reading)

# #----------------------------------------------------------------

all_reading = []
with open(fileno+'L_limping.json', 'r') as json_file:
    with open(fileno+'R_limping.json','r') as json_file2:
        data1 = json.load(json_file)
        data1 = data1['UsersData']['GCeG0u1ovpfUxScbzJYcEKgp4bq2']['readings']
        data2 = json.load(json_file2)
        data2 = data2['UsersData']['edpU0psG0NfcTLhIRAF20sGM7w53']['readings']
        count = 30
        for (reading1,reading2) in zip(data1,data2):
            one_reading = []
            reading = data1[reading1]
            one_reading.append(reading['Accangle1']['x'])
            one_reading.append(reading['Accangle1']['y'])
            one_reading.append(reading['Accangle2']['x'])
            one_reading.append(reading['Accangle2']['y'])
            one_reading.append(reading['Acceleration1']['x'])
            one_reading.append(reading['Acceleration1']['y'])
            one_reading.append(reading['Acceleration1']['z'])
            one_reading.append(reading['Acceleration2']['x'])
            one_reading.append(reading['Acceleration2']['y'])
            one_reading.append(reading['Acceleration2']['z'])
            one_reading.append(reading['Angle1']['x'])
            one_reading.append(reading['Angle1']['y'])
            one_reading.append(reading['Angle1']['z'])
            one_reading.append(reading['Angle2']['x'])
            one_reading.append(reading['Angle2']['y'])
            one_reading.append(reading['Angle2']['z'])
            one_reading.append(reading['Gyro1']['x'])
            one_reading.append(reading['Gyro1']['y'])
            one_reading.append(reading['Gyro1']['z'])
            one_reading.append(reading['Gyro2']['x'])
            one_reading.append(reading['Gyro2']['y'])
            one_reading.append(reading['Gyro2']['z'])
            one_reading.append(reading['distance1'])
            one_reading.append(reading['distance2'])
            one_reading.append(reading['voltage0'])
            one_reading.append(reading['voltage1'])
            one_reading.append(reading['voltage2'])

            reading = data2[reading2]
            one_reading.append(reading['Accangle1']['x'])
            one_reading.append(reading['Accangle1']['y'])
            one_reading.append(reading['Accangle2']['x'])
            one_reading.append(reading['Accangle2']['y'])
            one_reading.append(reading['Acceleration1']['x'])
            one_reading.append(reading['Acceleration1']['y'])
            one_reading.append(reading['Acceleration1']['z'])
            one_reading.append(reading['Acceleration2']['x'])
            one_reading.append(reading['Acceleration2']['y'])
            one_reading.append(reading['Acceleration2']['z'])
            one_reading.append(reading['Angle1']['x'])
            one_reading.append(reading['Angle1']['y'])
            one_reading.append(reading['Angle1']['z'])
            one_reading.append(reading['Angle2']['x'])
            one_reading.append(reading['Angle2']['y'])
            one_reading.append(reading['Angle2']['z'])
            one_reading.append(reading['Gyro1']['x'])
            one_reading.append(reading['Gyro1']['y'])
            one_reading.append(reading['Gyro1']['z'])
            one_reading.append(reading['Gyro2']['x'])
            one_reading.append(reading['Gyro2']['y'])
            one_reading.append(reading['Gyro2']['z'])
            one_reading.append(reading['distance1'])
            one_reading.append(reading['distance2'])
            one_reading.append(reading['voltage0'])
            one_reading.append(reading['voltage1'])
            one_reading.append(reading['voltage2'])

            all_reading.append(one_reading)
            count = count-1
            if(count==0):
              break
        while(count>0):
          count -= 1
          one_reading = []
          for i in range(54):
            one_reading.append(0.0)
          all_reading.append(one_reading)


labels.append(3)
inputs.append(all_reading)

# #----------------------------------------------------------------

all_reading = []
with open(fileno+'L_parkinsons.json', 'r') as json_file:
    with open(fileno+'R_parkinsons.json','r') as json_file2:
        data1 = json.load(json_file)
        data1 = data1['UsersData']['GCeG0u1ovpfUxScbzJYcEKgp4bq2']['readings']
        data2 = json.load(json_file2)
        data2 = data2['UsersData']['edpU0psG0NfcTLhIRAF20sGM7w53']['readings']
        count = 30
        for (reading1,reading2) in zip(data1,data2):
            one_reading = []
            reading = data1[reading1]
            one_reading.append(reading['Accangle1']['x'])
            one_reading.append(reading['Accangle1']['y'])
            one_reading.append(reading['Accangle2']['x'])
            one_reading.append(reading['Accangle2']['y'])
            one_reading.append(reading['Acceleration1']['x'])
            one_reading.append(reading['Acceleration1']['y'])
            one_reading.append(reading['Acceleration1']['z'])
            one_reading.append(reading['Acceleration2']['x'])
            one_reading.append(reading['Acceleration2']['y'])
            one_reading.append(reading['Acceleration2']['z'])
            one_reading.append(reading['Angle1']['x'])
            one_reading.append(reading['Angle1']['y'])
            one_reading.append(reading['Angle1']['z'])
            one_reading.append(reading['Angle2']['x'])
            one_reading.append(reading['Angle2']['y'])
            one_reading.append(reading['Angle2']['z'])
            one_reading.append(reading['Gyro1']['x'])
            one_reading.append(reading['Gyro1']['y'])
            one_reading.append(reading['Gyro1']['z'])
            one_reading.append(reading['Gyro2']['x'])
            one_reading.append(reading['Gyro2']['y'])
            one_reading.append(reading['Gyro2']['z'])
            one_reading.append(reading['distance1'])
            one_reading.append(reading['distance2'])
            one_reading.append(reading['voltage0'])
            one_reading.append(reading['voltage1'])
            one_reading.append(reading['voltage2'])

            reading = data2[reading2]
            one_reading.append(reading['Accangle1']['x'])
            one_reading.append(reading['Accangle1']['y'])
            one_reading.append(reading['Accangle2']['x'])
            one_reading.append(reading['Accangle2']['y'])
            one_reading.append(reading['Acceleration1']['x'])
            one_reading.append(reading['Acceleration1']['y'])
            one_reading.append(reading['Acceleration1']['z'])
            one_reading.append(reading['Acceleration2']['x'])
            one_reading.append(reading['Acceleration2']['y'])
            one_reading.append(reading['Acceleration2']['z'])
            one_reading.append(reading['Angle1']['x'])
            one_reading.append(reading['Angle1']['y'])
            one_reading.append(reading['Angle1']['z'])
            one_reading.append(reading['Angle2']['x'])
            one_reading.append(reading['Angle2']['y'])
            one_reading.append(reading['Angle2']['z'])
            one_reading.append(reading['Gyro1']['x'])
            one_reading.append(reading['Gyro1']['y'])
            one_reading.append(reading['Gyro1']['z'])
            one_reading.append(reading['Gyro2']['x'])
            one_reading.append(reading['Gyro2']['y'])
            one_reading.append(reading['Gyro2']['z'])
            one_reading.append(reading['distance1'])
            one_reading.append(reading['distance2'])
            one_reading.append(reading['voltage0'])
            one_reading.append(reading['voltage1'])
            one_reading.append(reading['voltage2'])

            all_reading.append(one_reading)
            count = count-1
            if(count==0):
              break
        while(count>0):
          count -= 1
          one_reading = []
          for i in range(54):
            one_reading.append(0.0)
          all_reading.append(one_reading)


labels.append(4)
inputs.append(all_reading)

# #----------------------------------------------------------------

all_reading = []
with open(fileno+'L_scissoring.json', 'r') as json_file:
    with open(fileno+'R_scissoring.json','r') as json_file2:
        data1 = json.load(json_file)
        data1 = data1['UsersData']['GCeG0u1ovpfUxScbzJYcEKgp4bq2']['readings']
        data2 = json.load(json_file2)
        data2 = data2['UsersData']['edpU0psG0NfcTLhIRAF20sGM7w53']['readings']
        count = 30
        for (reading1,reading2) in zip(data1,data2):
            one_reading = []
            reading = data1[reading1]
            one_reading.append(reading['Accangle1']['x'])
            one_reading.append(reading['Accangle1']['y'])
            one_reading.append(reading['Accangle2']['x'])
            one_reading.append(reading['Accangle2']['y'])
            one_reading.append(reading['Acceleration1']['x'])
            one_reading.append(reading['Acceleration1']['y'])
            one_reading.append(reading['Acceleration1']['z'])
            one_reading.append(reading['Acceleration2']['x'])
            one_reading.append(reading['Acceleration2']['y'])
            one_reading.append(reading['Acceleration2']['z'])
            one_reading.append(reading['Angle1']['x'])
            one_reading.append(reading['Angle1']['y'])
            one_reading.append(reading['Angle1']['z'])
            one_reading.append(reading['Angle2']['x'])
            one_reading.append(reading['Angle2']['y'])
            one_reading.append(reading['Angle2']['z'])
            one_reading.append(reading['Gyro1']['x'])
            one_reading.append(reading['Gyro1']['y'])
            one_reading.append(reading['Gyro1']['z'])
            one_reading.append(reading['Gyro2']['x'])
            one_reading.append(reading['Gyro2']['y'])
            one_reading.append(reading['Gyro2']['z'])
            one_reading.append(reading['distance1'])
            one_reading.append(reading['distance2'])
            one_reading.append(reading['voltage0'])
            one_reading.append(reading['voltage1'])
            one_reading.append(reading['voltage2'])

            reading = data2[reading2]
            one_reading.append(reading['Accangle1']['x'])
            one_reading.append(reading['Accangle1']['y'])
            one_reading.append(reading['Accangle2']['x'])
            one_reading.append(reading['Accangle2']['y'])
            one_reading.append(reading['Acceleration1']['x'])
            one_reading.append(reading['Acceleration1']['y'])
            one_reading.append(reading['Acceleration1']['z'])
            one_reading.append(reading['Acceleration2']['x'])
            one_reading.append(reading['Acceleration2']['y'])
            one_reading.append(reading['Acceleration2']['z'])
            one_reading.append(reading['Angle1']['x'])
            one_reading.append(reading['Angle1']['y'])
            one_reading.append(reading['Angle1']['z'])
            one_reading.append(reading['Angle2']['x'])
            one_reading.append(reading['Angle2']['y'])
            one_reading.append(reading['Angle2']['z'])
            one_reading.append(reading['Gyro1']['x'])
            one_reading.append(reading['Gyro1']['y'])
            one_reading.append(reading['Gyro1']['z'])
            one_reading.append(reading['Gyro2']['x'])
            one_reading.append(reading['Gyro2']['y'])
            one_reading.append(reading['Gyro2']['z'])
            one_reading.append(reading['distance1'])
            one_reading.append(reading['distance2'])
            one_reading.append(reading['voltage0'])
            one_reading.append(reading['voltage1'])
            one_reading.append(reading['voltage2'])

            all_reading.append(one_reading)
            count = count-1
            if(count==0):
              break
        while(count>0):
          count -= 1
          one_reading = []
          for i in range(54):
            one_reading.append(0.0)
          all_reading.append(one_reading)


labels.append(5)
inputs.append(all_reading)

#----------------------------------------------------------------
csv_file_path = fileno+'output.json'
label_file = fileno+'labels.json'
with open(csv_file_path, 'w') as f:
    json.dump(inputs,f)
with open(label_file, 'w') as f:
  json.dump(labels,f)