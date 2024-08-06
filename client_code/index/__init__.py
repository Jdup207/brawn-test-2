from ._anvil_designer import indexTemplate
from anvil import *
import anvil.server

  # Page 1, introduction page with abilities to go to all pages. With a quote.
class index(indexTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  # Page 2, Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

