from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..EntryEdit import EntryEdit
from ..DHForm import DHForm
from ..RLForm import RLForm
from ..RoExForm import RoExForm
from ..WPForm import WPForm

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    self.text_area_1.text="iSapiens Apps"
    self.job = None
    self.refresh_entries()
      # Set an event handler on the RepeatingPanel (our 'entries_panel')
    self.entries_panel.set_event_handler('x-delete-entry', self.delete_entry)
    

  def add_entry_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Initialise an empty dictionary to store the user inputs
    new_entry = {}
    if self.job == "DistrictHeating":
      
      # Open an alert displaying the 'DHForm' Form
      save_clicked = alert(
        content=DHForm(item=new_entry),
        title="Add Entry",
        large=True,
        buttons=[("Save", True), ("Cancel", False)]
      )
    # If the alert returned 'True', the save button was clicked.
    elif self.job == "RailRoad":
      
      # Open an alert displaying the 'DHForm' Form
      save_clicked = alert(
        content=RLForm(item=new_entry),
        title="Add Entry",
        large=True,
        buttons=[("Save", True), ("Cancel", False)]
      )
    elif self.job == "RoExAEEA":
      
      # Open an alert displaying the 'DHForm' Form
      save_clicked = alert(
        content=RoExForm(item=new_entry),
        title="Add Entry",
        large=True,
        buttons=[("Save", True), ("Cancel", False)]
      )
    elif self.job == "WaterPumping":
      
      # Open an alert displaying the 'DHForm' Form
      save_clicked = alert(
        content=WPForm(item=new_entry),
        title="Add Entry",
        large=True,
        buttons=[("Save", True), ("Cancel", False)]
      )
    else:
      # Open an alert displaying the 'EntryEdit' Form
      save_clicked = alert(
        content=EntryEdit(item=new_entry),
        title="Add Entry",
        large=True,
        buttons=[("Save", True), ("Cancel", False)]
      )
      # If the alert returned 'True', the save button was clicked.
    if save_clicked:
      anvil.server.call('add_entry', new_entry)
      self.refresh_entries()
    
  def refresh_entries(self):
     # Load existing entries from the Data Table, 
     # and display them in the RepeatingPanel
     self.entries_panel.items = anvil.server.call('get_entries')

  def delete_entry(self, entry, **event_args):
    # Delete the entry
    anvil.server.call('delete_entry', entry)
    # Refresh entry to remove the deleted entry from the Homepage
    self.refresh_entries()

  def selectRoExAEEA_click(self, **event_args):
    """This method is called when the button is clicked"""
    for x in [self.selectDH, self.selectRL, self.selectWP]:
      x.role = ""
    self.selectRoExAEEA.role = "outlined-button"
    self.text_area_1.text = app_tables.categories.get(name='roexaeea')['description'] #anvil.server.call('get_ExA_description')
    self.entries_panel.items = anvil.server.call('get_ExA_entries')
    self.job = "RoExAEEA"
    self.add_entry_button.enabled = True
    
  

  def selectRL_click(self, **event_args):
    """This method is called when the button is clicked"""
    for x in [self.selectDH, self.selectRoExAEEA, self.selectWP]:
      x.role = ""
    self.selectRL.role = "outlined-button"
    self.text_area_1.text = app_tables.categories.get(name='railroad')['description']
    self.entries_panel.items = anvil.server.call('get_RL_entries')
    self.job = "RailRoad"
    self.add_entry_button.enabled = True
  
  def selectDH_click(self, **event_args):
    """This method is called when the button is clicked"""
    for x in [self.selectRL, self.selectRoExAEEA, self.selectWP]:
      x.role = ""
    self.selectDH.role = "outlined-button"
    self.text_area_1.text = app_tables.categories.get(name='districtheating')['description']
    self.entries_panel.items = anvil.server.call('get_DH_entries')
    self.job = "DistrictHeating"
    self.add_entry_button.enabled = True

  def selectWP_click(self, **event_args):
    """This method is called when the button is clicked"""
    for x in [self.selectRL, self.selectRoExAEEA, self.selectDH]:
      x.role = ""
    self.selectWP.role = "outlined-button"
    self.text_area_1.text = app_tables.categories.get(name='waterpumping')['description']
    self.entries_panel.items = anvil.server.call('get_WP_entries')
    self.job = "WaterPumping"
    self.add_entry_button.enabled = True

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    filedata=file.get_bytes()
    anvil.server.call('read_categories_from_csv',filedata.decode())

  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    filedata=file.get_bytes()
    anvil.server.call('read_entries_from_csv',filedata.decode())

  def btnInitDBs_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('init_dbs')
    self.btnInitDBs.enabled = False

