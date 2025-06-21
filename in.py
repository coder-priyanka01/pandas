import pandas as pd

#df = pd.read_json("sample_Data.json")

data = {
    "Name" :['ram','shyam','ghanshyam'],
    "Age" : [10,20,30],
    "city": ['Nagpur','Mumbai','Delhi']
}

df = pd.DataFrame(data)

print('Displaying the info of data set')
print(df.info())