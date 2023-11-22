import pandas as pd
import numpy as np

# 1. Create a DataFrame with 3 columns and 50 rows
np.random.seed(42)
data = pd.DataFrame(np.random.rand(50, 3), columns=['Column1', 'Column2', 'Column3'])

# 2. Replace 10% of values with NaN
nan_indices = np.random.choice(range(50), size=int(0.1 * 50), replace=False)
data.iloc[nan_indices] = np.nan

# 3a. Identify and count missing values
missing_values = data.isnull().sum()
print("Missing values:")
print(missing_values)

# 3b. Drop columns with more than 5 null values
data = data.dropna(thresh=len(data) - 5, axis=1)

# 3c. Identify and drop the row with the maximum sum
max_sum_row_label = data.sum(axis=1).idxmax()
data = data.drop(index=max_sum_row_label)

# 3d. Sort the DataFrame based on the first column
data = data.sort_values(by='Column1')

# 3e. Remove duplicates from the first column
data = data.drop_duplicates(subset='Column1')

# 3f. Find correlation and covariance
correlation = data['Column1'].corr(data['Column2'])
covariance = data['Column2'].cov(data['Column3'])
print("\nCorrelation between Column1 and Column2:", correlation)
print("Covariance between Column2 and Column3:", covariance)

# 3g. Discretize the second column into 5 bins
data['Column2_bins'] = pd.cut(data['Column2'], bins=5)

# Display the modified DataFrame
print("\nModified DataFrame:")
print(data)
