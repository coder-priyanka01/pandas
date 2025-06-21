import pandas as pd

data = {
    "Name" :['ram','shyam','ghanshyam'],
    "Age" : [10,20,30],
    "city": ['Nagpur','Mumbai','Delhi']
}

df = pd.DataFrame(data)
print(df)

#df.to_csv("output.csv", index=False) # To save in csv file

#df.to_excel("output.xlsx")# Load and display Excel file

df.to_json("output.json", orient="records", indent=4)# Save to JSON file
print(df)