import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json
#from rlokt_wrapper_local import evaluate_rl_local

@anvil.server.callable
def calculate_railroad(params):
  #print(f"Params: {params}")
  par = json.loads(params)
  #return evaluate_rl_local(par)
  return evaluate_rl(par)

def evaluate_rl(par):
  res = f"Response for : {par['title']}\n"
  res = res + f"Input parameters: \n"
  res = res + f"Fuel cost = {par['cfuel']} [EUR/kg] \n"
  res = res + f"Electricity cost = {par['cel']} [EUR/kWh] \n"
  res = res + f"Number of tracks = {par['ntracks']} [EUR/kWh] \n"
  #res = res + f"L1 ="
  index = 1
  for l in par['mLoad']:
    res = res + f"L{index} = {l}"
    index = index + 1
  res = res +" [tons]\n"
  index = 1
  for a in par['L']:
    res = res + f"L{index} = {a}"
    index = index + 1
  res = res +" [km]\n"
  res = res + f"Number of trips per year = {par['ntrips']} [EUR/kWh] \n"
  #res = res + f"A1 = {par['A1']}, A2 = {par['A2']}, A3 = {par['A3']} [m2]\n"
  res = res + f"Calculated values ..."
  return res