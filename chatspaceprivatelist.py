# Import libraries
import googleapiclient.discovery
from googleapiclient.errors import HttpError
import csv

# Define API service name and version
SERVICE_NAME = 'chat'
VERSION = 'v1'

# Function to get a list of spaces
def get_spaces(credentials):
  """
  Retrieves a list of chat spaces using the Chat API.

  Args:
    credentials: Google API credentials object.

  Returns:
    A list of dictionaries representing chat spaces.
  """
  service = googleapiclient.discovery.build(SERVICE_NAME, VERSION, credentials=credentials)
  try:
    # Request spaces list
    results = service.spaces().list().execute()
    return results.get('spaces', [])
  except HttpError as error:
    print(f"An error occurred: {error}")
    return []

# Function to check space access and build CSV data
def check_spaces_and_build_csv(credentials, csv_file):
  """
  Checks accessState of spaces and builds a CSV with private ones.

  Args:
    credentials: Google API credentials object.
    csv_file: Path to the output CSV file.
  """
  spaces = get_spaces(credentials)
  data = []
  for space in spaces:
    if space.get('accessState') == 'PRIVATE':
      # Extract relevant space details
      name = space.get('name')
      space_id = space.get('name').split('/')[-1]
      data.append([name, space_id])

  # Write data to CSV
  with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Space Name', 'Space ID'])
    writer.writerows(data)
  print(f"Successfully created CSV file: {csv_file}")

# Replace with your actual credentials path
credentials_path = 'path/to/your/credentials.json'

# Read credentials from file
# (Follow instructions on obtaining credentials from https://developers.google.com/workspace)
# ...

# Set output CSV filename
csv_filename = 'private_spaces.csv'

check_spaces_and_build_csv(credentials, csv_filename)
