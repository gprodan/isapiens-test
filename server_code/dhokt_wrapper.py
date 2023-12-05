import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json
#import districtheating.DHaug-okt2023

@anvil.server.callable
def calculate_districtheating(params):
   #print(f"Params: {params}")
   par = json.loads(params)
#   T0 = float(par['T0'])
#   L1 = float(par['L1'])
#   L2 = float(par['L2'])
#   L3 = float(par['L3'])
#   A1 = float(par['A1'])
#   A2 = float(par['A2'])
#   A3 = float(par['A3'])
   
   return evaluate_dh(par)


def evaluate_dh(par):
  res = f"Response for : {par['title']}\n"
  res = res + f"Input parameters: \n"
  res = res + f"T0 = {par['T0']} [K] \n"
  #res = res + f"L1 ="
  for l in par['L']:
   res = res + "L{i} = {l[0]}" [m]\n"
  res = res +" [m]\n"
  res = res + f"A1 = {par['A1']}, A2 = {par['A2']}, A3 = {par['A3']} [m2]\n"
  res = res + f"Calculated values ..."
  return res