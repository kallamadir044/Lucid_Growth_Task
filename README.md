
# **Filter Companies by Services**
**Description**
This script filters companies from a CSV file based on specific services they offer. The script loads a CSV file named 'companies.csv', extracts the column names, defines a list of relevant services related to email marketing and management, filters the companies based on those services, and saves the filtered companies to a new CSV file named 'filtered_companies.csv'.

# Requirements
    * Python3
    * csv module (built-in)
# Usage
    1. Place the companies.csv file in the same directory as the script.
    2. Run the script using Python: python filter_companies.py
    3. The script will generate a new CSV file named filtered_companies.
    4. csv with the filtered companies.
# Script
**Step 1: Load the CSV file**
The script loads the 'companies.csv' file using the 'csv' module.


   'with open('companies.csv', 'r') as file:
       reader = csv.reader(file)
       companies = list(reader)'
     
**Step 2: Get the column names**
The script extracts the column names from the first row of the CSV file.


   'column_names = companies[0][1:]'
     
**Step 3: Define the relevant services**

The script defines a list of relevant services related to bulk email sending.


   'relevant_services = ['mass email', 'bulk email', 'high volume email sending', 'email blast services', 'Mail Transfer Agent', 'MTA configuration', 'MTA management', 'email system administration', 'email marketing', 'email infrastructure', 'email system assessment', 'email monitoring']'
     
**Step 4: Filter the companies**

The script filters the companies based on the presence of relevant services in their service offerings.


   'filtered_companies = [column_names]  # Add column names to the filtered list
   for company in companies[1:]:
       if any(service in company[2] for service in relevant_services):
           filtered_companies.append(company[1:])'
     
**Step 5: Save the filtered companies to a new CSV file**

The script saves the filtered companies to a new CSV file named 'filtered_companies.csv'.


   'with open('filtered_companies.csv', 'w', newline='') as file:
       writer = csv.writer(file)
       writer.writerows(filtered_companies)'
     
# Input

The script takes a CSV file named 'companies.csv'

# Output

The script generates a new CSV file named 'filtered_companies.csv' with the filtered companies. The output CSV file has the same columns as the input CSV file.
