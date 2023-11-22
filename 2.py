import pandas as pd

# a. Create a series with 5 elements, display the series sorted on index and values
series_a = pd.Series([3, 1, 5, 2, 4], index=['e', 'b', 'd', 'a', 'c'])

print("Original Series:")
print(series_a)

sorted_by_index = series_a.sort_index()
sorted_by_values = series_a.sort_values()

print("\nSorted Series by Index:")
print(sorted_by_index)

print("\nSorted Series by Values:")
print(sorted_by_values)

# b. Create a series with N elements with some duplicate values, find the minimum and maximum ranks
series_b = pd.Series([5, 2, 8, 2, 7, 4, 2, 9])

min_ranks = series_b.rank(method='first')
max_ranks = series_b.rank(method='max')

print("\nSeries with Ranks (First Method):")
print(min_ranks)

print("\nSeries with Ranks (Max Method):")
print(max_ranks)

# c. Display the index value of the minimum and maximum element of a Series
min_index = series_b.idxmin()
max_index = series_b.idxmax()

print("\nIndex of Minimum Element:", min_index)
print("Index of Maximum Element:", max_index)
