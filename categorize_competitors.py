import csv

# Load the CSV file
with open('companies.csv', 'r') as file:
    reader = csv.reader(file)
    companies = list(reader)

# Get the column names from the first row
column_names = companies[0][1:]

# Define the relevant services
relevant_services = ['mass email', 'bulk email', 'high volume email sending', 'email blast services', 'Mail Transfer Agent', 'MTA configuration', 'MTA management', 'email system administration', 'email marketing', 'email infrastructure', 'email system assessment', 'email monitoring']

# Filter the companies
filtered_companies = [column_names]  # Add column names to the filtered list
for company in companies[1:]:
    if any(service in company[2] for service in relevant_services):
        filtered_companies.append(company[1:])
        
# Save the filtered companies to a new CSV file
with open('filtered_companies.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(filtered_companies)
