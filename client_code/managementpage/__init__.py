from ._anvil_designer import managementpageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..logdate import logdate
from ..logdate_1 import logdate_1

  # page just existing
class managementpage(managementpageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #refresh the Data Grid, so all information saves.
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

  # log acitiy page
  def log_date_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    item = {}
    editing_form = logdate(item=item)

    #if the user clicks OK on the alert
    if alert(content=editing_form, large=True):
      anvil.server.call('log_management', item)
      #refresh the Data Grid, information save.
      self.repeating_panel_1.items = app_tables.management.search()


