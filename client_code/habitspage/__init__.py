from ._anvil_designer import habitspageTemplate
from anvil import *
import anvil.server

# Any code you write here will run before the form opens.
class habitspage(habitspageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  # How to get back to Home page
  def home_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('index')
    
  # How to get to Sport Page
  def sport_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('sportpage')

  # How to get to Management Page
  def management_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('managementpage')

  def habits_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('habitspage')


  # the page itself