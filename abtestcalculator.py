# import libraries
from scipy import stats
import numpy as np

# function to check for invalid inputs
def check_input(input_string):
    while True:
        try:
            value = int(input(input_string))
        except:
            print("Please input an integer from 1-100!")
            continue
        else:
            break
    return value
   
def getsamplesize(baseline_conversion_rate, minimum_detectable_effect, significance_threshold = 0.05):

    # lift desired
    alpha = significance_threshold
    desired_output = baseline_conversion_rate*(1+minimum_detectable_effect)

    # Default Value
    beta = 0.8 

    # pooled variance estimator formula
    pooled_variance_estimator = baseline_conversion_rate*(1-baseline_conversion_rate) + desired_output*(1-desired_output)

    # critical values of alpha and beta
    alpha_critical_value = round(stats.norm.ppf(1-alpha/2),2)
    beta_critical_value = round(stats.norm.ppf(beta),2)

    # sample size formula 
    sample_size = pooled_variance_estimator*pow(alpha_critical_value+beta_critical_value,2)/pow(desired_output-baseline_conversion_rate,2)
    rounded_sample_size = np.ceil(sample_size)

    return int(rounded_sample_size)

if __name__ == '__main__':
    # input by user 
    baseline_conversion_rate = check_input("Baseline Conversion Rate(%): ")/100
    minimum_detectable_effect = check_input("Minimum Detectable Effect(%): ")/100
    alpha = check_input("Significance Threshold(%): ")/100

    # Output
    value = getsamplesize(baseline_conversion_rate, minimum_detectable_effect, alpha)
    print(f'The sample size of each variation: {value}')