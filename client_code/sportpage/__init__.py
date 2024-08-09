from ._anvil_designer import sportpageTemplate
from anvil import *
import anvil.server


class sportpage(sportpageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
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

  def sport_button_click(self, **event_args):
    #clicking on this will do nothing as the user is currently on this page
    pass
