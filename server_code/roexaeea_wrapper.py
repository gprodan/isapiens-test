import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.

@anvil.server.callable
def sections():
   return 8

@anvil.server.callable
def title():
   return 'Romania ExA & EEA'

@anvil.server.callable
def calculate_roexaeea(params):
   #print(f"Params: {params}")
   par = json.loads(params)
  
   return evaluate_dh(par)


def evaluate_dh(par):
  res = f"Response for : {par['title']}\n"
  res = res + f"Input parameters: \n"
  res = res + f"Nw = {par['Nw']} \n"
  res = res + f"wkhrs = {par['wkhrs']} \n"
  res = res + f"exchg = {par['exchg']} \n"
  res = res + f"s = {float(par['s'])*12*float(par['exchg'])} \n"
  res = res + f"M2 = {par['M2']} \n"
  res = res + f"Calculated values ..."
  return res



