# Import libraries
import googleapiclient.discovery
from googleapiclient.errors import HttpError

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

# Function to update space access settings to private
def update_space_to_private(credentials, space_id):
  """
  Attempts to update a space's accessState to 'PRIVATE' using spaces.patch.

  Args:
    credentials: Google API credentials object.
    space_id: The ID of the space to modify.

  Returns:
    None
  """
  service = googleapiclient.discovery.build(SERVICE_NAME, VERSION, credentials=credentials)
  try:
    # Update space with accessState set to 'PRIVATE'
    body = {'accessState': 'PRIVATE'}
    service.spaces().patch(name=f'spaces/{space_id}', updateMask='accessState', body=body).execute()
    print(f"Successfully set accessState to 'PRIVATE' for space: {space_id}")
  except HttpError as error:
    print(f"An error occurred updating space {space_id}: {error}")

# Function to check spaces and update access
def check_spaces_and_update_access(credentials):
  """
  Checks spaces and attempts to update accessState to 'PRIVATE' for non-private ones.

  Args:
    credentials: Google API credentials object.
  """
  spaces = get_spaces(credentials)
  for space in spaces:
    if space.get('accessState') != 'PRIVATE':
      space_id = space.get('name').split('/')[-1]
      update_space_to_private(credentials, space_id)

# Replace with your actual credentials path
credentials_path = 'path/to/your/credentials.json'

# Read credentials from file
# (Follow instructions on obtaining credentials from https://developers.google.com/workspace)
# ...

check_spaces_and_update_access(credentials)
