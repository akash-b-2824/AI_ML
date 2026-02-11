#Task 2: The Grade Filter (Boolean Masking & Missing Data)
import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])
print("Original Series:")
print(grades)
print("\nMissing Values (isnull):")
print(grades.isnull())
print("\nFilled Series (fillna):")
grades.fillna(0, inplace=True)
print(grades)
print("\nFiltered Scores (greater than 60):")
filtered_scores = grades[grades > 60]
print(filtered_scores)