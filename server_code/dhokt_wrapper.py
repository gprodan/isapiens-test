import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json
#from dhokt_wrapper_local import evaluate_dh_local

@anvil.server.callable
def calculate_districtheating(params):

  par = json.loads(params)
 
  #return evaluate_dh_local(par)
  return evaluate_dh(par)


def evaluate_dh(par):
  res = f"Response for : {par['title']}\n"
  res = res + f"Input parameters: \n"
  res = res + f"T0 = {par['T0']} [K] \n"
  #res = res + f"L1 ="
  index = 1
  for l in par['L']:
    res = res + f"L{index} = {l}"
    index = index + 1
  res = res +" [m]\n"
  index = 1
  for a in par['A']:
    res = res + f"A{index} = {a}"
    index = index + 1
  res = res +" [m2]\n"

  #res = res + f"A1 = {par['A1']}, A2 = {par['A2']}, A3 = {par['A3']} [m2]\n"
  res = res + f"Calculated values ..."
  return res