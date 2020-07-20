from cap_one_initial_dive import df_s_and_d as df

""" 
I need to figure out how to delete the header rows with all the NaN values.
print(df.iloc[0:12]) shows first data value of -0.5 in last column.
"""
df.drop([0,1,2,3,4,5,6,7,8,9,10], axis=0, inplace=True)
#print(df[:3])

""" 
Drop all the school and district data with less than 16 valid scores.
'num_valid_scores' column name
"""
def drop_unusable(x):
    """ 
    Input
    Output
     """