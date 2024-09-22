from ._anvil_designer import logdateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

  # form just existing
class logdate(logdateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  # go back to the previous page.
  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('managementpage')
