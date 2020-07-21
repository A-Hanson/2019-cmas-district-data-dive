import pandas as pd
from cap_one_initial_dive import df_s_and_d as df

'''
Need to eliminate all the <16 values from table before export to CSV
668 values to be eliminated
'''
df = df[df['num_valid_scores'] != '< 16']

'''
Split into two dataframes: schools and districts
district_df shape = (554, 26)
school_df shape = (3484, 26)
'''
district_df = df[df['school_code'] == '0000']
school_df = df[df['school_code'] != '0000']

'''
Drop rows with '- -' values in the 'num_ee_19' column.
district_df_ee shape = (195, 26)
school_df_ee shape = (1053, 26)
'''
district_df_ee = district_df[district_df['num_ee_19'] != '- -']
school_df_ee = school_df[school_df['num_ee_19'] != '- -']


'''
Drop rows with '- -' values in the 'num_me_or_ee_19' column.
district_df_ee shape = (508, 26)
school_df_ee shape = (2996, 26)
'''
district_df_me_ee = district_df[district_df['num_me_or_ee_19'] != '- -']
school_df_me_ee = school_df[school_df['num_me_or_ee_19'] != '- -']
print(district_df_me_ee.shape)

#if __name__ == "__main__":
    #df['num_valid_scores'] = df['num_valid_scores'].map({'< 16': NaN})
        
    #print(rows_to_drop)
    #print(df['num_valid_scores'].sort_values().head())
    #print(df['num_valid_scores' ].value_counts())
    #print(school_df.shape)
    #print(df[df['num_valid_scores'] != '< 16'].shape)