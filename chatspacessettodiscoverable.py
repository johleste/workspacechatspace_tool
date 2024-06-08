import csv

def update_csv_access(csv_file, target_audience):
  """
  This function takes a CSV file path and a target audience string as input.
  It reads the CSV file, updates the accessState of each space to "discoverable",
  adds the target audience to the accessList, and writes the changes to a new CSV file.
  It also retrieves the space ID from the first column.

  Args:
      csv_file (str): Path to the CSV file containing space data.
      target_audience (str): String representing the target audience to grant access.
  """
  # Read the CSV data
  with open(csv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)
    space_ids = [row[reader.fieldnames[0]] for row in data]  # Extract space IDs

  # Update accessState and accessList for each space
  for i, row in enumerate(data):
    space_id = space_ids[i]  # Use corresponding space ID for this row
    row['accessState'] = 'discoverable'
    access_list = row.get('accessList', [])
    access_list.append(target_audience)
    row['accessList'] = access_list

  # Write the updated data to a new CSV file (prevents modifying original file)
  new_file = f"{csv_file[:-4]}_updated.csv"
  with open(new_file, 'w', newline='') as csvfile:
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

  print(f"CSV data updated successfully! Check '{new_file}' for changes.")
    
# Replace 'your_csv_file.csv' with the actual path to your CSV file
# Replace 'your_target_audience' with the target audience string (e.g., 'emea@company.com')
update_csv_access('your_csv_file.csv', 'your_target_audience')

# This script uses the spaces.patch method conceptually, but it modifies the CSV data directly.
# Implementing the spaces.patch method would require a specific API library for the workspace management tool you're using.
