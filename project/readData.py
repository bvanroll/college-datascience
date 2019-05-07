import pandas as pd


with open("DataScienceData01.txt","r") as infile:
    lines = infile.readlines()



def dataParse(l):
    objs = l.split("& ")
    dic = {}
    for obj in objs:
        items = obj.split("=")
        title = items[0]
        data = items[1].split(",")
        if len(data) == 1:
            data = data[0]
        dic[title] = data
    return dic 


data = []
for l in lines:
   data.append(dataParse(l))

df = pd.DataFrame(data)
print(df)
