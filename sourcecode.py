import pandas as pd
import matplotlib.pyplot as plt

# Load the sewer pipes dataset
pipes = pd.read_csv('/Users/jainish/Downloads/Sewer_Pipes.csv')

# Safe Conversion of ConstructionDate

# Print first few rows to inspect ConstructionDate
print(pipes['ConstructionDate'].head())

# Step 1: Convert ConstructionDate to numeric safely
# If it's a year, this works; if it's a date, we'll extract the year
pipes['ConstructionDate'] = pd.to_datetime(pipes['ConstructionDate'], errors='coerce')

# Step 2: Extract year
pipes['ConstructionYear'] = pipes['ConstructionDate'].dt.year

# Step 3: Now calculate Pipe Age
current_year = 2025
pipes['Pipe_Age'] = current_year - pipes['ConstructionYear']


# Categorize pipes based on Diameter
def categorize_diameter(diameter):
    if diameter < 300:
        return 'Small'
    elif diameter < 600:
        return 'Medium'
    else:
        return 'Large'

pipes['Size_Category'] = pipes['Diameter'].apply(categorize_diameter)

# Show basic statistics
print("=== Sewer Pipe Material Distribution ===")
print(pipes['Material'].value_counts())
print("\n=== Pipe Size Categories ===")
print(pipes['Size_Category'].value_counts())

# Plot: Distribution of Pipe Ages
pipes['Pipe_Age'].hist(bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of Sewer Pipe Ages')
plt.xlabel('Pipe Age (Years)')
plt.ylabel('Number of Pipes')
plt.grid(False)
plt.show()

# Plot: Pipe Material Breakdown
material_counts = pipes['Material'].value_counts()
material_counts.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Sewer Pipe Materials Used')
plt.xlabel('Material Type')
plt.ylabel('Number of Pipes')
plt.xticks(rotation=45)
plt.grid(False)
plt.show()

# Plot: Pipe Size Category Pie Chart
size_counts = pipes['Size_Category'].value_counts()
size_counts.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Pipe Diameter Size Categories')
plt.ylabel('')  # Remove default y-label
plt.show()

# Save the enhanced dataset
pipes.to_csv('processed_sewer_pipes.csv', index=False)

print("\nProcessed sewer pipe data saved successfully to 'processed_sewer_pipes.csv'.")
