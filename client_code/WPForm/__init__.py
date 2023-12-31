from ._anvil_designer import WPFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json

class WPForm(WPFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # self.categories = app_tables.categories.get(name='districtheating')
    self.item['category'] = app_tables.categories.get(name='waterpumping')


  def viewResult_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def sendParams_click(self, **event_args):
    """This method is called when the button is clicked"""
    pr = dict()
    if self.txtFormated.text:
      params = self.txtFormated.text
    else:
      pr['title'] = self.txtTitle.text
      pr['T0'] = float(self.txtTempAmb.text if self.txtTempAmb.text else 300.0)
      pr['L0'] = self.txtLengths.text if self.txtLengths.text else "[500.0,300.0,1000.0]"
      pr['L'] = self.txtLengthsP.text if self.txtLengthsP.text else "[200.0,400.0,600.0]"
      pr['m'] = self.txtMassFlow.text if self.txtMassFlow.text else "[10.0,15.0,30.0]"
      params = json.dumps(pr, indent = 4)
    self.item['title'] = self.txtTitle.text
    self.item['content'] = str(params)
    res = anvil.server.call('calculate_waterpumping', params=params)
    self.item['result'] = res
    self.results.text = res
