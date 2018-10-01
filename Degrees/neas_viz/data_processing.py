import pandas as pd
import os
cwd = os.getcwd()
print(cwd)
neas_df = pd.read_csv("Degrees/neas_viz/data/PUF_FinalCSV.CSV")
num_rows = neas_df.shape[0]
neas_df = neas_df.fillna({"Q39_EARNINGS":-3, "Q38_HOURS_WORKED":-3,
    "Q37_WEEKS_WORKED":-3, "Q36_FULL_TIME":-3, "Q35_EMPLOYED":-3,
    })
### Preprocessing: Bin Q38_HOURS_WORKED, the report has individual values
hours_worked_bins = ["Did not work","1-9","10-19","20-29","30-39", "40-49","50-59","60-69",
                                    "70-79", "80-89","90-99",">100"]
neas_df['Q38_HOURS_WORKED_BINS'] = pd.cut(neas_df['Q38_HOURS_WORKED'],
                                    [-100,0,10,20,30,40,50,60,70,80,90,100,2000],
                                    labels=hours_worked_bins)
def get_responses(target, options,ids):
    '''Generic function to summarize the responses for the target column,
    given the options selected for each id (input column). Response is the
    number of entries in each category, so that a bar chart can be plotted'''
    if target is "Q38_HOURS_WORKED":
        target = "Q38_HOURS_WORKED_BINS"
    selection = [True for _ in range(num_rows)]
    for id, opt in zip(ids, options) :
        # If no options are selected for a particular question,
        # consider all of them to be true
        if opt:
            # Do a logical "and" on all the checkboxes selected
            selection = [a and b for a, b in zip(selection, neas_df[id].isin(opt).tolist())]
    response = neas_df[selection][target].value_counts(dropna=False)
    data = response.sort_index().tolist()
    print(target, " : ", response)
    print(target," : ",data)
    return data

def get_q39_earnings_ymax():
    return max(neas_df["Q39_EARNINGS"].value_counts(dropna=False).tolist())

def get_q37_weeks_ymax():
    return max(neas_df["Q37_WEEKS_WORKED"].value_counts(dropna=False).tolist())

def get_q38_hours_ymax():
    return max(neas_df["Q38_HOURS_WORKED_BINS"].value_counts(dropna=False).tolist())
  
def get_q38_hours_xrange():
    return hours_worked_bins