import pandas as pd
from cap_one_initial_dive import df_s_and_d as df
from initial_clean import DataFilter




def filter_high_perf_schools(obj):
    obj.exceeded_expectations()
    obj.filter_for_school()
    obj.filter_out_all_grades()
    return obj

def filter_met_or_exceed_expectations_schools(obj):
    obj.met_or_exceeded_expectations()
    obj.filter_for_school()
    obj.filter_out_all_grades()
    return obj
    

def districts_with_ten_or_more_results(obj):
    pass #maybe come back to
    obj = obj.df.groupby('district_name').count()
    obj = obj.query('level >= 10')
    return obj


if __name__ == "__main__":
    test = DataFilter(df)
    #districts_with_ten_or_more_results(test)
    #print(test.df.shape)
    #high_perf_schools = DataFilter(df)
    #filter_high_perf_schools(high_perf_schools)
    #high_perf_dist_count = high_perf_schools.df.groupby('district_name').count()
    #print(high_perf_schools.df.info())
    #passing_schools = DataFilter(df)
    #filter_met_or_exceed_expectations_schools(passing_schools)
    #participation_rate(passing_schools)
    #passing_schools.df['participation_rate'].unique()
    #print(passing_schools.df.shape)
    #print(high_perf_schools.df['participation_rate'].shape)