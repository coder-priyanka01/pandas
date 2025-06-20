import pandas as pd

df_customers = pd.DataFrame({
    "CustomerId":[1,2,3],
    "Name":["Ramesh","Suresh","Kalpesh"]
})

df_orders = pd.DataFrame({
        "CustomerId":[1,2,4],
        "OrderAmount":[250,450,350]
})
#df_merged = pd.merge(df_customers, df_orders, on = "CustomerId", how = "inner")
#print("inner join")

#df_merged = pd.merge(df_customers, df_orders, on = "CustomerId", how = "outer")
#print("outer join")

#df_merged = pd.merge(df_customers, df_orders, on = "CustomerId", how = "left")
#print("left join")

df_merged = pd.merge(df_customers, df_orders, on = "CustomerId", how = "right")
print("right join")
print(df_merged)
