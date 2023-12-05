import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json 

@anvil.server.callable
def calculate_waterpumping(params):
   #print(f"Params: {params}")
   par = json.loads(params)
   return evaluate_wp(par)


def evaluate_wp(par):
  res = f"Response for : {par['title']}\n"
  res = res + f"Input parameters: \n"
  res = res + f"T0 = {par['T0']} [K] \n"
  #res = res + f"L1 ="
  index = 1
  for l in par['L0']:
    res = res + f"L{index} = {l}"
    index = index + 1
  res = res +" [m]\n"
  index = 1
  for l in par['L']:
    res = res + f"L{index} = {l}"
    index = index + 1
  res = res +" [m]\n"
  index = 1
  for a in par['m']:
    res = res + f"A{index} = {a}"
    index = index + 1
  res = res +" [kg/s]\n"
  res = res + f"Calculated values ..."
  return res
