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
    self.item['category'] = app_tables.categories.get(name='roexaeea')


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
      pr['Nw'] = float(self.txtWrkPop.text if self.txtWrkPop.text else 300.0)
      pr['wkhrs'] = float(self.txtWrkHours.text if self.txtWrkHours.text else 1783.0)
      pr['exchg'] = float(self.txtExchange.text if self.txtExchange.text else 0.2)
      pr['s'] = float(self.txtSalary.text if self.txtSalary.text else 4000.0)
      pr['M2'] = float(self.txtM2Coef.text if self.txtM2Coef.text else 422691000000.0)
      params = json.dumps(pr, indent = 4)
    self.item['title'] = self.txtTitle.text
    self.item['content'] = str(params)
    res = anvil.server.call('calculate_roexaeea', params=params)
    self.item['result'] = res
    self.results.text = res
