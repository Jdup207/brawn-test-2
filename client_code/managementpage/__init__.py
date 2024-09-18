from ._anvil_designer import managementpageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..logdate import logdate
from ..logdate_1 import logdate_1

class managementpage(managementpageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #refresh the Data Grid
    self.repeating_panel_1.items = app_tables.management.search()

  # How to get back to Home page
  def home_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('index')
    
  # How to get to Sport Page
  def sport_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('sportpage')

  # How to get to Habits Page
  def habits_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('habitspage')

  # how to get to Management Page
  def management_button_click(self, **event_args):
    #clicking on this will do nothing as the user is currently on this page
    pass

  def log_date_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    item = {}
    editing_form = logdate_1(item=item)

    #if the user clicks OK on the alert
    if alert(content=editing_form, large=True):
      #add the movie to the Data Table with the filled in information
      anvil.server.call('log_management', item)
      #refresh the Data Grid
      self.repeating_panel_1.items = app_tables.management.search()


