from ._anvil_designer import sportpageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..logactivities import logactivities

class sportpage(sportpageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.repeating_panel_1.items = app_tables.activites.search()
  
  # How to get back to Home page
  def home_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('index')

  # How to get to Habits
  def habits_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('habitspage')

  # How to get to Management
  def management_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('managementpage')
  #  open_form('logactivities')

  # Here users already are on sport page, will do nothing on click.
  def sport_button_click(self, **event_args):
    #clicking on this will do nothing as the user is currently on this page
    pass


  # the page itself
  # How to get to login activity page
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    #open_form('logactivities')
   # open_form('logactivities')
    item = {}
    editing_form = logactivities(item=item)
    alert(content=editing_form, large=True)

  def summary_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('activitysummary')
