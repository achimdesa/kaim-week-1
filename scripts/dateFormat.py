import pandas as pd
from datetime import datetime

# Function to convert date format
def convert_date_format(date_str):
    try:
        # Parse the date string
        date_obj = datetime.fromisoformat(date_str)
        # Return the formatted date
        return date_obj.strftime("%d/%m/%Y")
    except ValueError:
        return date_str  # Return original if there's an error

# Read the CSV file
input_file = 'E:\\EDUCATION\\Kifiya_AI_Mastery_Program\\W1Data\\Data\\raw_analyst_ratings.csv\\stock_filtered.csv'  
output_file = 'E:\\EDUCATION\\Kifiya_AI_Mastery_Program\\W1Data\\Data\\raw_analyst_ratings.csv\\output.csv'  

df = pd.read_csv(input_file)

# Assuming the date column is named 'date_column'
# Replace 'date_column' with the actual name of your date column
df['date'] = df['date'].apply(convert_date_format)

# Save the modified DataFrame to a new CSV file
df.to_csv(output_file, index=False)

print(f"Date format converted and saved to {output_file}")