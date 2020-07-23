import pandas as pd
from src.cap_one_initial_dive import df_s_and_d as df

class DataFilter(object):
    '''
    Returns dataframe with rows filtered out based for having no scores for certain categories
    Makes a copy, then makes changes to that object's data frame
    '''
    def __init__(self, df):
        self.self = self
        self.df = df.copy()
        self.clear_less_than_16_valid_scores()
        self.map_over_str_values()
        self.convert_to_float_and_int()
    
    def clear_less_than_16_valid_scores(self):
        '''
        Schools or districts with less than 16 valid scores obscure data for privacy.
        This filters out those rows.
        '''
        self.df = self.df[self.df['num_valid_scores'] != '< 16']
        return self.df

    def map_over_str_values(self):
        '''
        replaces '- -' string with a zero
        '''
        self.df = self.df.replace(['- -'], 0)
        self.df = self.df.fillna(0)
        return self.df

    def convert_to_float_and_int(self):
        '''
        Columns with numerical data converted to floats and integers
        '''
        self.df['num_total_rec'] = self.df['num_total_rec'].astype(int, errors='ignore')
        self.df['num_valid_scores'] = self.df['num_valid_scores'].astype(int, errors='ignore')
        self.df['num_no_scores'] = self.df['num_no_scores'].astype(int, errors='ignore')
        self.df['participation_rate'] = self.df['participation_rate'].astype(float, errors='ignore')
        self.df['mean_scale_score_19'] = self.df['mean_scale_score_19'].astype(int, errors='ignore')
        self.df['std_scale_score_19'] = self.df['std_scale_score_19'].astype(int, errors='ignore')
        self.df['mean_scale_score_18'] = self.df['mean_scale_score_18'].astype(int, errors='ignore')
        self.df['num_pme_19'] = self.df['num_pme_19'].astype(int, errors='ignore')
        self.df['percent_pme_19'] = self.df['percent_pme_19'].astype(float, errors='ignore')
        self.df['num_ae_19'] = self.df['num_ae_19'].astype(int, errors='ignore')
        self.df['percent_ae_19'] = self.df['percent_ae_19'].astype(float, errors='ignore')
        self.df['num_me_19'] = self.df['num_me_19'].astype(int, errors='ignore')
        self.df['percent_me_19'] = self.df['percent_me_19'].astype(float, errors='ignore')
        self.df['num_ee_19'] = self.df['num_ee_19'].astype(int, errors='ignore')
        self.df['percent_ee_19'] = self.df['percent_ee_19'].astype(float, errors='ignore')
        self.df['num_me_or_ee_19'] = self.df['num_me_or_ee_19'].astype(int, errors='ignore')
        self.df['percent_me_or_ee_19'] = self.df['percent_me_or_ee_19'].astype(float, errors='ignore')
        self.df['num_me_or_ee_18'] = self.df['num_me_or_ee_18'].astype(int, errors='ignore')
        self.df['percent_me_or_ee_18'] = self.df['percent_me_or_ee_18'].astype(float, errors='ignore')
        self.df['change_in_me_or_ee'] = self.df['change_in_me_or_ee'].astype(float, errors='ignore')
        return self.df
    
    def exceeded_expectations(self):
        self.df = self.df[self.df['num_ee_19'] != 0]
        return self.df

    def met_expectations(self):
        self.df = self.df[self.df['num_me_19'] != 0]
        return self.df
    
    def met_or_exceeded_expectations(self):
        '''
        returns rows with data in the met or exceeded expectations 2019 column
        '''
        self.df = self.df[self.df['num_me_or_ee_19'] != 0]
        return self.df
    
    def approached_expectations(self):
        self.df = self.df[self.df['num_ae_19'] != 0]
        return self.df
    
    def partially_met_expectations(self):
        self.df = self.df[self.df['num_pme_19'] != 0]
        return self.df
    
    def filter_for_state(self):
        self.df = self.df[self.df['level'] == 'STATE']
        return self.df
    
    def filter_for_district(self):
        self.df = self.df[self.df['level'] == 'DISTRICT']
        return self.df

    def filter_for_school(self):
        self.df = self.df[self.df['level'] == 'SCHOOL']
        return self.df

    def filter_for_all_grades(self):
        self.df = self.df[self.df['grade'] == 'All Grades']
        return self.df
    
    def filter_out_all_grades(self):
        self.df = self.df[self.df['grade'] != 'All Grades']
        return self.df
    
    def filter_for_high_school(self):
        self.df = self.df[self.df['grade'] == 'HS']
        return self.df
    
    def filter_for_middle_school(self):
        self.df = self.df[self.df['grade'] == '08']
        return self.df
    
    def filter_for_elem_school(self):
        self.df = self.df[self.df['grade'] == '05']
        return self.df


if __name__ == "__main__":
    test = DataFilter(df)
    test.filter_for_district()
    test.filter_for_all_grades()
    print(test.df['participation_rate'].describe())
    print(test.df['mean_scale_score_19'].describe())
    #me_or_ee = test.met_or_exceeded_expectations().head()
    #print(me_or_ee.head())
    #df['num_valid_scores'] = df['num_valid_scores'].map({'< 16': NaN})
        
    #print(rows_to_drop)
    #print(df['num_valid_scores'].sort_values().head())
    #print(df['num_valid_scores' ].value_counts())
    #print(school_df.shape)
    #print(df[df['num_valid_scores'] != '< 16'].shape)