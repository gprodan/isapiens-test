from ._anvil_designer import RoExFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json

class RoExForm(RoExFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # self.categories = app_tables.categories.get(name='districtheating')
    self.item['category'] = app_tables.categories.get(name='districtheating')


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
      pr['L'] = self.txtLengths.text if self.txtLengths else [1000.0, 2000.0, 3000.0]
      pr['A'] = self.txtUsersArea.text if self.txtUsersArea else [3000.0, 2000.0, 12000.0]
      params = json.dumps(pr, indent = 4)
    self.item['title'] = self.txtTitle.text
    self.item['content'] = params
    res = anvil.server.call('calculate_districtheating', params=params)
    self.item['result'] = res
    self.results.text = res