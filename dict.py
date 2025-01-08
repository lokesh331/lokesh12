import pandas as pd 
reduce_mobile_usage=[2,4,6]
sleep_hours=[8,9,10]
students_data=["lokesh","mintu","hemanth"]
dict={
    "reduce_mobile_usage":reduce_mobile_usage,
    "sleep_hours":sleep_hours,
    "students_data":students_data
}
df=pd.DataFrame(dict)
print(df)