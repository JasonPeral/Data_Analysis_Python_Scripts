import pandas as pd
import numpy as np

np.random.seed(42)

# Creating the database
data = {
    'id': list(range(1, 21)),  # Create a list for mutable id
    'numerical_column1': np.random.randint(1, 100, size=20).astype(float),  # Convert to float
    'numerical_column2': np.random.rand(20) * 100,
    'categorical_column': np.random.choice(['A', 'B', 'C'], size=20)
}

# Introducing some missing files
data['numerical_column1'][5] = np.nan
data['numerical_column2'][10] = np.nan

data['id'][15] = 5  # Duplicate id

# Saving the frame
df = pd.DataFrame(data)

#Saving the dataset to synthetic_dataset.csv
df.to_csv('synthetic_dataset.csv', index=False)

# Displaying the dataset
print("Synthetic Dataset for Data Cleaning:")
print(df)