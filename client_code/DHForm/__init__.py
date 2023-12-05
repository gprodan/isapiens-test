from ._anvil_designer import DHFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class DHForm(DHFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def viewResult_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def sendParams_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.txtFormated.text:
      params = self.txtFormated.text
    else:
      pr['T0'] = float(self.txtTempAmb.text if self.txtTempAmb.text else 300.0)
      pr['L'] = self.txtLengths.text if self.txtLengths else [1000.0, 2000.0, 3000.0]
      pr['A'] = self.txtUsersArea.text if self.txtUsersArea else [3000.0, 2000.0, 12000.0]
      params = pr

    res = anvil.server.call('calculate_districtheating', params=params)
    self.results.text = res
