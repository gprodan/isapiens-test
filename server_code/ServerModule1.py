import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import csv
import pandas as pd

@anvil.server.callable
def read_categories_from_csv(csv_string):
  csv_list=csv_string.split()
  cr=csv.reader(csv_list)
    
  for csv_line in cr:
    try:
      app_tables.categories.add_row(name=csv_line[0], description=csv_line[1])
    except:
      pass

@anvil.server.callable
def read_entries_from_csv(csv_string):
  csv_list=csv_string.split()
  cr=csv.reader(csv_list)
    
  for csv_line in cr:
     try: 
      app_tables.categories.add_row(title=csv_line[0], 
                                  content=csv_line[1], 
                                  created=csv_line[2], 
                                  updated=csv_line[3], 
                                  category=csv_line[4], result=csv_line[5])
     except:
       pass

      
@anvil.server.callable
def add_entry(entry_dict):
  app_tables.entries.add_row(
    created=datetime.now(),
    **entry_dict
  )

@anvil.server.callable
def init_dbs():
  import_csv_data("categories.csv", app_tables.categories)
  import_csv_data("entries.csv", app_tables.entries)

def import_csv_data(file, table):
  with open(file, "r") as f:
    df = pd.read_csv(f)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      
      table.add_row(**d)

@anvil.server.callable
def get_entries():
  # Get a list of entries from the Data Table, sorted by 'created' column, in descending order
  return app_tables.entries.search(
    tables.order_by("created", ascending=False)
  )

@anvil.server.callable
def get_ExA_description():
  # Get a list of entries from the Data Table, sorted by 'created' column, in descending order
  return app_tables.categories.get(name='roexaeea')['description']

@anvil.server.callable
def get_ExA_entries():
  # Get a list of roexaeea simulations 
  return app_tables.entries.search(
    category=app_tables.categories.get(name='roexaeea')
  )

@anvil.server.callable
def get_DH_entries():
  return app_tables.entries.search(
    category=app_tables.categories.get(name='districtheating')
  )

@anvil.server.callable
def get_WP_entries():
  return app_tables.entries.search(
    category=app_tables.categories.get(name='waterpumping')
  )

@anvil.server.callable
def get_RL_entries():
  return app_tables.entries.search(
    category=app_tables.categories.get(name='railroad')
  )

  
@anvil.server.callable
def update_entry(entry, entry_dict):
  # check that the entry given is really a row in the ‘entries’ table
  if app_tables.entries.has_row(entry):
    entry_dict['updated'] = datetime.now()
    entry.update(**entry_dict)
  else:
    raise Exception("Entry does not exist")

@anvil.server.callable
def delete_entry(entry):
  # check that the entry being deleted exists in the Data Table
  if app_tables.entries.has_row(entry):
    entry.delete()
  else:
    raise Exception("Entry does not exist")