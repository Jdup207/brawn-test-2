from ._anvil_designer import activitysummaryTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..logactivities import logactivities

  # the page existing
class activitysummary(activitysummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #refresh the Data Grid, so the progress saves.
    self.repeating_panel_1.items = app_tables.activites.search()

  # how to log in activity
  def log_activity_click(self, **event_args):
      #pass in an empty dictionary to MovieEdit
    item = {}
    editing_form = logactivities(item=item)
    
    # if the user clicks OK on the alert
    if alert(content=editing_form, large=True):
      anvil.server.call('log_activity', item)
      #refresh the Data Grid, so information saves.
      self.repeating_panel_1.items = app_tables.activites.search()

  # to go back to sport page.
  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('sportpage')
