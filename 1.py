import numpy as np

# a. Create a two-dimensional array (ARR1), compute mean, standard deviation, and variance along the second axis
ARR1 = np.random.rand(3, 4)
mean_arr1 = np.mean(ARR1, axis=1)
std_dev_arr1 = np.std(ARR1, axis=1)
variance_arr1 = np.var(ARR1, axis=1)

print("ARR1:")
print(ARR1)
print("\nMean along second axis:", mean_arr1)
print("Standard Deviation along second axis:", std_dev_arr1)
print("Variance along second axis:", variance_arr1)

# b. Create a 2-dimensional array, print shape, type, and data type, reshape it based on user inputs
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))
ARR2 = np.random.randint(0, 10, size=(m, n))

print("\nARR2:")
print(ARR2)
print("Shape of ARR2:", ARR2.shape)
print("Type of ARR2:", type(ARR2))
print("Data type of ARR2:", ARR2.dtype)

n, m = map(int, input("\nEnter new dimensions (n m): ").split())
ARR2_reshaped = ARR2.reshape((n, m))

print("\nARR2 Reshaped:")
print(ARR2_reshaped)

# c. Test whether elements of a given 1D array are zero, non-zero, and NaN. Record indices of these elements
ARR3 = np.array([1, 0, 3, 0, np.nan, 5, 0])

zero_indices = np.where(ARR3 == 0)[0]
nonzero_indices = np.where(ARR3 != 0)[0]
nan_indices = np.where(np.isnan(ARR3))[0]

print("\nZero Indices:", zero_indices)
print("Non-zero Indices:", nonzero_indices)
print("NaN Indices:", nan_indices)

# d. Create three random arrays and perform operations
Array1 = np.random.rand(5)
Array2 = np.random.rand(5)
Array3 = np.random.rand(5)

Array4 = Array3 - Array2
Array5 = 2 * Array1

covariance = np.cov(Array1, Array4)[0, 1]
correlation = np.corrcoef(Array1, Array5)[0, 1]

print("\nArray1:", Array1)
print("Array2:", Array2)
print("Array3:", Array3)
print("Array4 (Array3 - Array2):", Array4)
print("Array5 (2 * Array1):", Array5)
print("Covariance between Array1 and Array4:", covariance)
print("Correlation between Array1 and Array5:", correlation)

# e. Create two random arrays, find sum of the first half and product of the second half
Array6 = np.random.rand(10)
Array7 = np.random.rand(10)

sum_first_half = np.sum(Array6[:5]) + np.sum(Array7[:5])
product_second_half = np.prod(Array6[5:]) * np.prod(Array7[5:])

print("\nArray6:", Array6)
print("Array7:", Array7)
print("Sum of the first half:", sum_first_half)
print("Product of the second half:", product_second_half)

# f. Create an array with random values, determine the size of the memory occupied by the array
Array8 = np.random.rand(4, 3)
memory_size = Array8.nbytes

print("\nArray8:")
print(Array8)
print("Size of the memory occupied by Array8:", memory_size, "bytes")

# g. Create a 2-dimensional array, swap two rows, reverse a specified column, and store in another variable
ARR4 = np.random.randint(10, 100, size=(4, 5))

print("\nARR4 (Original):")
print(ARR4)

# Swap two rows (row 1 and row 2)
ARR4_swapped_rows = ARR4.copy()
ARR4_swapped_rows[1, :], ARR4_swapped_rows[2, :] = ARR4_swapped_rows[2, :].copy(), ARR4_swapped_rows[1, :].copy()

# Reverse a specified column (column 3)
ARR4_reversed_column = ARR4.copy()
ARR4_reversed_column[:, 2] = np.flip(ARR4_reversed_column[:, 2])

print("\nARR4 (Swapped Rows):")
print(ARR4_swapped_rows)
print("\nARR4 (Reversed Column):")
print(ARR4_reversed_column)
