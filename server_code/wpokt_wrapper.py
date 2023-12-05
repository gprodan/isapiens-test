import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json 

@anvil.server.callable
def calculate_waterpumping(params):
   print(f"Params: {params}")
   par = json.loads(params)
   x = float(par['x'])
   y = float(par['y'])
   return f"Evaluated y({x}) = {x*x-3*x+2}"
