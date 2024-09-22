from ._anvil_designer import indexTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

  # Page 1, introduction page with abilities to go to all pages. With a quote.
class index(indexTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  # Page 2, Any code you write here will run before the form opens.
  # How to get to my sportpage. Sport button
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('sportpage')
    
  # How to get to my habitspage. habits button
  def habits_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('habitspage')

  # How to get to my management page. management button
  def management_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('managementpage')




