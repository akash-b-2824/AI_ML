#Task 3: The Username Formatter (Vectorized String Operations)
import pandas as pd
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
cleaned_usernames = usernames.str.strip().str.lower()
print(cleaned_usernames)
contains_a = cleaned_usernames.str.contains('a')
print(contains_a)