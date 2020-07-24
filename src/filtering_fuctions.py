import pandas as pd
from src.cap_one_initial_dive import df_s_and_d as df
from src.initial_clean import DataFilter
import scipy.stats as stats
import matplotlib.pyplot as plt

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

def binomial_test_graph(data, prob=0.5, end_range=110):
    n = find_num_trials_district(data)
    k = find_num_met_or_exceeds_district(data)
    binomial = stats.binom(n, prob)
    fig, ax = plt.subplots(1, figsize=(16, 8))
    bars = ax.bar(range(n+1), [binomial.pmf(i) for i in range(n+1)],
             align="center")
    ax.set_xlim(0, end_range)

    ax.axvline(k, linewidth=3, color='green', linestyle= "--", label='Actual Number of Districts that Met or Exceeded Expectations')

    ax.set_xlabel('Number of Districts', fontsize=20)
    ax.set_ylabel('Probability', fontsize=20)
    ax.set_title("Districts that Met or Exceeded Expectations Under the Null Hypothesis", fontsize = 25)
    ax.legend()
    plt.tight_layout()
    plt.show()
    prob_equal_or_more_extreme = 1 - binomial.cdf(k-1)
    print("Probability of Observing Data Equal or More Extreme than Actual: {:2.2}".format(prob_equal_or_more_extreme))

def find_name_met_or_exceeds_district(obj):
    k = district_scores_all_grades(obj)
    k = k[k['mean_scale_score_19'] >= met_expectations]
    k = k['district_name']
    return k
    
def export_state_csv(obj):
    obj.filter_for_state()
    return obj.df.to_csv('../data/state_data.csv')

def export_district_csv(obj):
    obj.filter_for_district()
    return obj.df.to_csv('../data/district_data.csv')

def export_school_csv(obj):
    obj.filter_for_school()
    return obj.df.to_csv('../data/school_data.csv')

if __name__ == "__main__":
    test = DataFilter(df)
    export_district_csv(test)
    export_school_csv(test)
    export_state_csv(test)
    #print(find_name_met_or_exceeds_district(test))
    #print(binomial_test_graph(test))
    #print(district_scores_all_grades(test))
    #n = find_num_trials_district(test)
    #k = find_num_met_or_exceeds_district(test)
    #p = 0.5
    #binomial = stats.binom(n, p)
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