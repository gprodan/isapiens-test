import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.

@anvil.server.callable
def sections():
   return 8

@anvil.server.callable
def title():
   return 'Romania ExA & EEA'
  




