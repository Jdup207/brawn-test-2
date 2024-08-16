from ._anvil_designer import activitysummaryTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..logactivities import logactivities


class activitysummary(activitysummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def log_activity_click(self, **event_args):
      #pass in an empty dictionary to MovieEdit
    item = {}
    editing_form = logactivities(item=item)
    
    #if the user clicks OK on the alert
    if alert(content=editing_form, large=True):
      #add the movie to the Data Table with the filled in information
      anvil.server.call('log_activity', item)
      #refresh the Data Grid
      self.repeating_panel_1.items = app_tables.activites.search()
