import pandas as pd

# Load the CSV file into a DataFrame
csv_file_path = 'friendtech.csv'
dataframe = pd.read_csv(csv_file_path)

# Extract the 'address' and 'twitterUsername' columns
colonne_address = dataframe['address']
colonne_twitter = dataframe['twitterUsername']

# Define the target Twitter username to search
# Exemple: if the twitterUsername is @elonmusk so enter without the @
twitter = "LapepiteCrypto"   

def search(twitter):
    for index, elem in enumerate(colonne_twitter):
        if elem == twitter:
            address = colonne_address[index]
            print(f"The Twitter username '{twitter}' is associated with the address '{address}'.")
            return
        else: 
            print(f"The Twitter username '{twitter}' was not found in the data.")  
            return

search(twitter)
