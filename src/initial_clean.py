import pandas as pd
from cap_one_initial_dive import df_s_and_d as df

class DataFilter(object):
    '''
    Returns dataframe with rows filtered out based for having no scores for certain categories
    Makes a copy, then makes changes to that object's data frame
    '''
    def __init__(self, df):
        self.self = self
        self.df = df.copy()
        self.clear_less_than_16_valid_scores()
    
    def clear_less_than_16_valid_scores(self):
        '''
        Schools or districts with less than 16 valid scores obscure data for privacy.
        This filters out those rows.
        '''
        self.df = self.df[self.df['num_valid_scores'] != '< 16']
        return self.df
    
    def exceeded_expectations(self):
        self.df = self.df[self.df['num_ee_19'] != '- -']
        return self.df

    def met_expectations(self):
        self.df = self.df[self.df['num_me_19'] != '- -']
        return self.df
    
    def met_or_exceeded_expectations(self):
        '''
        returns rows with data in the met or exceeded expectations 2019 column
        '''
        self.df = self.df[self.df['num_me_or_ee_19'] != '- -']
        return self.df
    
    def approached_expectations(self):
        self.df = self.df[self.df['num_ae_19'] != '- -']
        return self.df
    
    def partially_met_expectations(self):
        self.df = self.df[self.df['num_pme_19'] != '- -']
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
    test.filter_for_school()
    print(test.df.head())
    #me_or_ee = test.met_or_exceeded_expectations().head()
    #print(me_or_ee.head())
    #df['num_valid_scores'] = df['num_valid_scores'].map({'< 16': NaN})
        
    #print(rows_to_drop)
    #print(df['num_valid_scores'].sort_values().head())
    #print(df['num_valid_scores' ].value_counts())
    #print(school_df.shape)
    #print(df[df['num_valid_scores'] != '< 16'].shape)