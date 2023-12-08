from ._anvil_designer import RLFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json

class RLForm(RLFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # self.categories = app_tables.categories.get(name='districtheating')
    self.item['category'] = app_tables.categories.get(name='railroad')


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
      pr['cfuel'] = float(self.txtFuelCost.text if self.txtFuelCost.text else 1.7)
      pr['cel'] = float(self.txtElCost.text if self.txtElCost.text else 0.17)
      pr['ntracks'] = float(self.txtNoTracks.text if self.txtNoTracks.text else 3)
      pr['mLoad'] = self.txtMassLoad.text if self.txtMassLoad else [2500,3000.0,2500.0]
      pr['L'] = self.txtRouteLength.text if self.txtRouteLength else [150.0,180.0,230.0]
      pr['ntrips'] = float(self.txtNoTrips.text if self.txtNoTrips.text else 60)
      params = json.dumps(pr, indent = 4)
    self.item['title'] = self.txtTitle.text
    self.item['content'] = str(params)
    res = anvil.server.call('calculate_railroad', params=params)
    self.item['result'] = res
    self.results.text = res
