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

def participation_rate(obj):
    pass
    obj = obj.df.copy()
    obj.df.drop(columns = [
                'level',
                'district_code',
                'district_name',
                'school_code',
                'num_total_rec',
                'num_no_scores',
                'mean_scale_score_19', #what am I doing])


if __name__ == "__main__":
    high_perf_schools = DataFilter(df)
    filter_high_perf_schools(high_perf_schools)
    passing_schools = DataFilter(df)
    filter_met_or_exceed_expectations_schools(passing_schools)
    passing_schools.df.drop()
    #print(passing_schools.df.shape)
    #print(high_perf_schools.df['participation_rate'].shape)