import pandas as pd
import random
import statsmodels.api as sm
# Create a list of years from 1679 to 2022
years = list(range(1679, 2023))

data = {
    'Year': years,
    'Population Growth': [random.uniform(0.5, 2.5) for _ in years],
    'Urbanization Rate': [random.uniform(0.1, 0.9) for _ in years],
    'Household Waste (tons)': [random.randint(1000, 50000) for _ in years],
    'General Waste (tons)': [random.randint(1000, 50000) for _ in years],
}




# Generate "Total Waste" to be directly proportional to the year
year_to_total_waste_ratio = 100  # Adjust this factor as needed
data['Total Waste (tons)'] = [year * year_to_total_waste_ratio + random.randint(100, 500) for year in data['Year']]

# Create a DataFrameq
df = pd.DataFrame(data)

print(df)
# Save the DataFrame to a CSV file
df.to_csv('proportional_waste_data.csv', index=False)








# Load the generated CSV file into a DataFrame
df = pd.read_csv('proportional_waste_data.csv')

# Define the independent variables (X) and the dependent variable (y)
X = df[['Population Growth', 'Urbanization Rate', 'Household Waste (tons)', 'General Waste (tons)']]
y = df['Total Waste (tons)']

# Add a constant to the independent variables (intercept term)
X = sm.add_constant(X)

# Fit the multiple linear regression model
model = sm.OLS(y, X).fit()

# Print the regression summary
print(model.summary())




# Assuming the model is already loaded (as shown in the previous example)

# Define the feature values for the year 2050
# You need to replace these values with your own input data for that year
population_growth_2050 = 1.5  # Replace with the population growth for 2050
urbanization_rate_2050 = 0.8  # Replace with the urbanization rate for 2050
household_waste_2050 = 25000  # Replace with the household waste for 2050
general_waste_2050 = 28000    # Replace with the general waste for 2050

# Create a DataFrame with the feature values for 2050
feature_values_2050 = pd.DataFrame({
    'Year': [2050],  # Add the year as an index
    'Population Growth': [population_growth_2050],
    'Urbanization Rate': [urbanization_rate_2050],
    'Household Waste (tons)': [household_waste_2050],
    'General Waste (tons)': [general_waste_2050]
})

# Make a prediction for the Total Waste in 2050
total_waste_2050_prediction = model.predict(feature_values_2050)

# # Print the prediction
# print(f"Predicted Total Waste for 2050: {total_waste_2050_prediction.values[0]:.2f} tons")

total_waste_2050 = total_waste_2050_prediction.values[0]

if total_waste_2050 >= 1e9:
    total_waste_2050_str = f"{total_waste_2050 / 1e9:.2f} billion metric tons"
elif total_waste_2050 >= 1e6:
    total_waste_2050_str = f"{total_waste_2050 / 1e6:.2f} million metric tons"
else:
    total_waste_2050_str = f"{total_waste_2050:.2f} metric tons"

print(f"Predicted Total Waste for 2050: {total_waste_2050_str}")
predicted_waste_2050 = total_waste_2050_str
asterisk_representation = '*' * len(predicted_waste_2050)

print(f"Predicted Total Waste for 2050: {asterisk_representation}")


def print_bordered_waste_basket(text):
    width = len(text) + 4
    basket_top = " " + "_" * (width + 4) + " "
    basket_empty = f"| {' ' * width} |"
    basket_content = f"| <{text}> |"

    print(basket_top)
    print(basket_empty)
    print(basket_content)
    print(basket_empty)
    print(basket_top)

total_waste_2050_str = f"{total_waste_2050_str}"

print_bordered_waste_basket(total_waste_2050_str)

