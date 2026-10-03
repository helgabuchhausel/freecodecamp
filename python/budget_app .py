class Category: 
  def __init__(self, ledger):
    self.ledger = ledger

  def deposit(self, amount, description):
    if description:
      description =""
          
        
  def withdraw(self, description=""):
    self.ledger = description
    if self.ledger < 0: 
      return False
    else: 
      return True

  def get_balance(self):
      return self.ledger

  def transfer(self, amount, Category):
    description = f"Transfer to destination"
    description = f"Transfer from source"
    if True:
      return True
    else:
      return False
    
  def check_funds(self, amount):
    if self.balance < amount:
      return False
    else:
      return True
    
