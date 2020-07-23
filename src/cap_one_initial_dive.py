import pandas as pd
#df_gender = pd.read_excel('2019 CMAS Science Disaggregated District and School Achievement Results.xlsx')
df_s_and_d = pd.read_excel('../data/2019_CMAS_Science_District_and_School_Achievement_Results.xlsx')
#renaming
""" 
Abbrevations used
19 = 2019
18 = 2018
pme = partially met expectations
ae = approached expectations
me = met expectations
ee = exceeded expectations
me_or_ee = met or exceeded expectations """

df_s_and_d.rename(columns={'Unnamed: 0': 'level', 'Unnamed: 1': 'district_code'}, inplace=True)
df_s_and_d.rename(columns={'Unnamed: 2': 'district_name', 'Unnamed: 3': 'school_code'}, inplace=True)
df_s_and_d.rename(columns={'Unnamed: 4': 'school_name'}, inplace=True)
df_s_and_d.rename(columns={'Unnamed: 5': 'grade', 'Unnamed: 6': 'num_total_rec'}, inplace=True)
df_s_and_d.rename(columns={'Unnamed: 7': 'num_valid_scores', 'Unnamed: 8': 'num_no_scores'}, inplace=True)
df_s_and_d.rename(columns={'Unnamed: 9': 'participation_rate', 'Unnamed: 10': 'mean_scale_score_19'}, inplace=True)
df_s_and_d.rename(columns={'Unnamed: 11': 'std_scale_score_19', 'Unnamed: 12': 'mean_scale_score_18'}, inplace=True)
df_s_and_d.rename(columns={'Unnamed: 13': 'num_pme_19', 'Unnamed: 14': 'percent_pme_19'}, inplace=True)
df_s_and_d.rename(columns={'Unnamed: 15': 'num_ae_19', 'Unnamed: 16': 'percent_ae_19'}, inplace=True)
df_s_and_d.rename(columns={'Unnamed: 17': 'num_me_19', 'Unnamed: 18': 'percent_me_19'}, inplace=True)
df_s_and_d.rename(columns={'Unnamed: 19': 'num_ee_19', 'Unnamed: 20': 'percent_ee_19'}, inplace=True)
df_s_and_d.rename(columns={'Unnamed: 21': 'num_me_or_ee_19', 'Unnamed: 22': 'percent_me_or_ee_19'}, inplace=True)
df_s_and_d.rename(columns={'Unnamed: 23': 'num_me_or_ee_18', 'Unnamed: 24': 'percent_me_or_ee_18'}, inplace=True)
df_s_and_d.rename(columns={'Unnamed: 25': 'change_in_me_or_ee'}, inplace=True)

print(df_s_and_d.columns)

""" 
I need to figure out how to delete the header rows with all the NaN values.
print(df.iloc[0:12]) shows first data value of -0.5 in last column.
"""
df_s_and_d.drop([0,1,2,3,4,5,6,7,8,9,10], axis=0, inplace=True)
#print(df_s_and_d[:3])


