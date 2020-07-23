import pandas as pd
from src.cap_one_initial_dive import df_s_and_d as df
from src.initial_clean import DataFilter
import scipy.stats as stats

met_expectations = 650

def district_scores_all_grades(obj):
    obj.filter_for_district()
    obj.filter_for_all_grades()
    return obj.df

def find_num_trials_district(obj):
    n = district_scores_all_grades(obj)
    n = int(n['level'].count())
    return n

def find_num_met_or_exceeds_district(obj):
    k = district_scores_all_grades(obj)
    k = k[k['mean_scale_score_19'] >= met_expectations]
    k = int(k['level'].count())
    return k
    
#H0 50% probability that a district met or exceeded expectations
#n = find_num_trials_district
#k = find_num_met_or_exceeds_district
#p = 0.5

if __name__ == "__main__":
    test = DataFilter(df)
    #print(district_scores_all_grades(test))
    n = find_num_trials_district(test)
    k = find_num_met_or_exceeds_district(test)
    p = 0.5
    binomial = stats.binom(n, p)
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