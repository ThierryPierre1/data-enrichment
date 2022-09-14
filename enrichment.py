import pandas as pd

## load in the data sets
discharges = pd.read_csv('Data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv')
discharges
discharges.dtypes

census = pd.read_csv('Data/NY_2019_ADI_9 Digit Zip Code_v3.1.txt')
census
census.dtypes

# List columns
discharges.columns
census.columns

# Creat smaller datasets
discharges_small = discharges[['Zip Code - 3 digits', 'Facility Name', 'Age Group']]
print(discharges_small.to_markdown())

census_small = census[['ZIPID', 'FIPS.x', 'Unnamed: 0']]
print(census_small.to_markdown())

# Merge the datasets
combined_df = pd.merge(discharges_small, census_small, how='left', left_on='ZIPID', right_on='Zip Code - 3 digits')

# Display the combined dataset
combined_df
