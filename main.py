import pandas as pd
import numpy as np
import random

# 1. read in citation pairs by year
# each row is one patent and one of it's citations
# patent #, patent year, patent tech class, citation patent #, citatation patent tech class

# one io table per YEAR

# From is the horizontal
# To is the vertical

#    T1 T2 T3
# T1
# T2 X
# T3

# ex.) T1 Borrows from T2 X amount
# X = count of rows/ instances


# 1. Pairs Dataframe (assumes well formed data)

#takes unclean data and outputs dataframe

tech_classes = ["A","B","C"]
years = ["2019", "2020", "2021"]


# processes patent data and retruns a dataframe with citation pairs
def process_pairs(raw_data: pd.DataFrame):
    pairs = pd.DataFrame(columns=["Year","Patent_Num", "Pat_Tech_Class", "Citation_Pat_Num", "Citation_Pat_Tech_Class"])

    # g patent data as base -> to get pairs, need g_us_patent citation. merge based on patent id -> merge with g_wipo technology for tech classes

    return pairs


# creates input output table
# outputs dataframe
def io_table(pairs: pd.DataFrame, year):
    num_tc = len(tech_classes)
    matrix = np.zeros((num_tc, num_tc))

    for i, x in enumerate(tech_classes):
        filtered = (filter_class_year(pairs, x, year))
        pr = patent_reference(filtered)
        matrix[i, :] += pr
        
    
    df_matrix = pd.DataFrame(matrix, columns=tech_classes)
    return df_matrix

# returns filtered dataframe by specific tech class and year
def filter_class_year(pairs, tc: str, yr: int):
    yr_str = str(yr)
    filt = pairs[(pairs["Pat_Tech_Class"] == tc) & (pairs["Year"] == yr_str)]
    return filt

# finding 'row' of io table
# input is only for one tech class AND year
# returns an array 
def patent_reference(fil_pairs: pd.DataFrame):
    ref = []

    for x in tech_classes:
        ref.append(fil_pairs[fil_pairs["Citation_Pat_Tech_Class"] == x]['Patent_Num'].count())
    
    return ref




################

# create a pool of patent IDs to draw from
patent_pool = [f"P{100000 + i}" for i in range(1, 200)]

rows = []
for i in range(500):
    year = random.choice(years)
    patent_num = random.choice(patent_pool)
    pat_tc = random.choice(tech_classes)
    citation_pat_num = random.choice(patent_pool)
    citation_tc = random.choice(tech_classes)
    rows.append({
        "Year": year,
        "Patent_Num": patent_num,
        "Pat_Tech_Class": pat_tc,
        "Citation_Pat_Num": citation_pat_num,
        "Citation_Pat_Tech_Class": citation_tc
    })

sample_df = pd.DataFrame(rows, columns=["Year", "Patent_Num", "Pat_Tech_Class", "Citation_Pat_Num", "Citation_Pat_Tech_Class"])

# inspect
# print(sample_df.shape)
# print(sample_df)

########

for year in years:
    print(year)
    print(io_table(sample_df, year))

