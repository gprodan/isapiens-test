from ._anvil_designer import EntryEditTemplate
from anvil import *
import anvil.server
from anvil.tables import app_tables


class EntryEdit(EntryEditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.categories = [(cat['name'], cat) for cat in app_tables.categories.search()]
    self.category_box.items = self.categories

  def image_uploader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.item['image'] = file

  
  def editParams_click(self, **event_args):
    """This method is called when the button is clicked"""
    editFormNames = {'roexaeea':'RoExAEEAForm','railroad':'RLForm','districtheating':'DHForm','waterpumping':'WPForm'}
    name = self.category_box.selected_value
    print(f"Category {name['name']} selected")
    
    #self.add_component(open_form(editFormNames[name['name']]))

  def calculate_click(self, **event_args):
    """This method is called when the button is clicked"""
    editFormNames = {'roexaeea':'calculate_roexeeea',
                     'railroad':'calculate_railroad',
                     'districtheating':'calculate_districtheating',
                     'waterpumping':'calculate_waterpumping'}
    name = self.category_box.selected_value
    print(f"{type(str(editFormNames[name['name']]))}, {type(editFormNames[name['name']])}")
    res = anvil.server.call(str(editFormNames[name['name']]), params=self.content_box.text)
    self.results.text = res





