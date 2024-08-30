import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def log_activity(activity_data):
  if activity_data.get('activity_name') and activity_data.get('activity_location') and activity_data.get('activity_time') and activity_data.get('activity_skills'):
      app_tables.activites.add_row(**activity_data)

@anvil.server.callable
def log_management(management_data):
  if management_data.get('date') and management_data.get('description'):
      app_tables.management.add_row(**management_data)
